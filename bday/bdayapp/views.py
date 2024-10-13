from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import EventForm
from django.contrib.auth.models import User
from .models import Event
from django.core.mail import send_mail
from background_task import background
from background_task.models import Task
import datetime
running=0

@background(schedule=5)
def sendmail():
    day=datetime.datetime.now().day
    month=datetime.datetime.now().month
    #print(day,month)
    events=Event.objects.filter(event_date__day=day,event_date__month=month)
    for event in events:
        print(f"{event.event_type} Reminder!",f"Event:{event.event_type}\nName:{event.person_name}\nDate:{event.event_date}")
        send_mail(f"{event.event_type} Reminder!",f"Event:{event.event_type}\nName:{event.person_name}\nDate:{event.event_date}","s.aditya49chn@gmail.com",[event.author.email])

@background(schedule=5)
def sendmailtest():
    print("Hey")
    #send_mail(f"{event.event_type} Reminder!",f"Event:{event.event_type}\nName:{event.person_name}\nDate:{event.event_date}","s.aditya49chn@gmail.com",[event.author.email])

@login_required
def home(request):
    author=User.objects.get(username=request.user)
    events=Event.objects.filter(author=author).order_by('event_date__month', 'event_date__day')
    context={'user':request.user,'events':events}
    return render(request,"bdayapp/mainpage.html",context)

@login_required
def addevent(request):
    context={'user':request.user}
    author=User.objects.get(username=request.user)
    if request.method=="POST":
        request.POST=request.POST.copy()
        request.POST['author']=author
        form=EventForm(request.POST)
    else:
        form=EventForm({'author':author})
    form.fields['author'].widget.attrs['disabled'] = True
    if form.is_valid():
        form.save()
        return redirect("/")
    context['form']= form
    return render(request,"bdayapp/newevent.html",context)


def createaccount(request):
    context={}
    error=""
    if request.method=="POST":
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        confpassword=request.POST['confpassword']
        if len(password)<7:
            error+="Password must atleast be 7 characters in length. "
        if password!=confpassword:
            error+="Passwords don't match. "
        userse = User.objects.filter(email=email)
        usersu = User.objects.filter(username=username)
        if len(userse)+len(usersu)>1:
            error+="User already exists. Log in instead."
        if not error:
            User.objects.create_user(username,email,password)
            send_mail("Thanks for creating your account!","This is to confirm your account has been created!","s.aditya49chn@gmail.com",[email])
            return redirect("/accounts/login")
    context["error"]=error
    return render(request,"bdayapp/createaccount.html",context)

def startitup(request):
    tasks = Task.objects.filter(verbose_name="wishes")
    sendmailtest(repeat=5)
    if len(tasks) == 0:
        sendmail(repeat=Task.DAILY,verbose_name="wishes")
    return redirect("/")