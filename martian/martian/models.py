from django.contrib.auth.models import User
from django.forms import ModelForm
from django.db import models


class UserForm(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(blank=True, max_length=30)
    password = models.CharField(blank=True, max_length=30)

class RequestForm(ModelForm):
    class Meta:
        model = UserForm
        fields = ['username','password',]
        

    