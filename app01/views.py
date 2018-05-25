# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from .models import File, Info, version
from django.views.decorators import csrf
from datetime import datetime
from django import forms
from xlrd import xldate_as_tuple
import MySQLdb.cursors
import xlsxwriter
import xlrd
import time
import os

username_t = 'root'

def ymlogin(request):
    context = {"error":0}
    #print request.method
    if request.method == "POST":
        input_name = request.POST[u'username']
        input_pwd = request.POST[u'password']
        result = authenticate(username=input_name,password=input_pwd)  
        if result:
            global username_t
            username_t = input_name
            context ["username"] = username_t
            login(request,result)
            return redirect("/index/",{'username':username_t})
        else:
            context['error'] = 1
            return render(request,'login.html',context)
    return render(request,'login.html',context)

@login_required
def upload(request):
    if request.is_ajax():
        obj = request.FILES.get('f')
        print obj
        f = open(os.path.join('upload',obj.name),'wb')
        for line in obj.chunks():
            f.write(line)
        f.close()
        return HttpResponse("文件上传成功")
    if request.method == 'GET':
        return render(request,'upload.html')
    return render(request,'upload.html')

@login_required
def index(request):
    infos = Info.objects.all()
    return render(request, 'index.html', context={'infos':infos})
    

    

