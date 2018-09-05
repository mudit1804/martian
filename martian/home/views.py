# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post, PostForm
from django.http import HttpResponse, HttpResponseRedirect
import datetime




# Create your views here.

@login_required(login_url='/$/')
def home(request):
    allposts = Post.objects.all()
    currentuser = request.user
    print currentuser
    if request.method == 'POST':
    
        form = PostForm(request.POST)
        if form.is_valid():
            now = datetime.datetime.now()
            dt = str(now.day) + '-' + str(now.month) + '-' + str(now.year) + ' ' + 'at' + ' ' + str(now.hour) + ':' + str(now.minute)
            print "form is valid"
            descr = form.cleaned_data['desc']
            newentry = Post(uname=currentuser,desc=descr,created_at=dt)
            newentry.save()
            return HttpResponseRedirect('/home/')
        else:
            print form.errors
    else:
        form = PostForm()
    return render(request, 'home/dashboard.html',{'allposts': allposts})

@login_required(login_url='/$/')
def like(request, id):
    allposts = Post.objects.all()
    mypost = Post.objects.get(pk=id)
    mypost.likes = mypost.likes + 1
    mypost.save()
    return render(request, 'home/dashboard.html',{'allposts': allposts})

@login_required(login_url='/$/')
def dislike(request, id):
    allposts = Post.objects.all()
    mypost = Post.objects.get(pk=id)
    mypost.dislikes = mypost.dislikes + 1
    mypost.save()
    return render(request, 'home/dashboard.html',{'allposts': allposts})








# def post(request):
#     print "yoo"
#     posts = Post.objects.all()
#     if request.method == 'POST':
#         print "hry post"
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/home/')
#     else:
#         form = PostForm()
#     return render(request, 'home/dashboard.html',{'form' : form})

