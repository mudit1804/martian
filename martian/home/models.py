# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm


# Create your models here.

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    uname = models.CharField(blank=True, max_length=30)
    desc = models.CharField(blank=True, max_length=10000)
    likes = models.IntegerField(blank=True, default=0)
    dislikes = models.IntegerField(blank=True, default=0)
    comment1 = models.CharField(blank=True,  max_length=1000)
    comment2 = models.CharField(blank=True,  max_length=1000)
    created_at = models.CharField(blank=True,  max_length=1000)


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['uname','desc','likes','dislikes','comment1','comment2','created_at']




    
