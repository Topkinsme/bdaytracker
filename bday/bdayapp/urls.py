from django.urls import path,include

from . import views

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("", views.home, name="home"),
    path("new/",views.createaccount,name="createaccount"),
    path("addevent/",views.addevent,name="addevent"),
    path("startitup/",views.startitup,name="startitup"),
]