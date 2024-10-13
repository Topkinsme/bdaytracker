from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):

    BDAY = "BIRTHDAY"
    WDAY = "WED-ANNI"
    MISC = "MISC"

    CHOICES = (
        (BDAY, "Birthday"),
        (WDAY, "Wedding Anniversary"),
        (MISC, "Misc"),
    )

    person_name=models.CharField(max_length=100)
    event_type=models.CharField(max_length=10,choices=CHOICES)
    event_date=models.DateField()
    author=models.ForeignKey(User,on_delete=models.CASCADE)
