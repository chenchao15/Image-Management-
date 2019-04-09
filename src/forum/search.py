# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render, get_object_or_404, redirect
from .models import Picture, Reply
from .forms import PostForm, ReplyForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect

def Get_pic_label(str):
    if str == "美女":
        return "girl"
    elif str =="帅哥":
        return "boy"
    elif str == "花":
        return "flower"
    else:
        return "animal"


def datasearch(request):
    if 'localplace' in request.GET:
        message = request.GET['localplace']
    else:
        message = '你提交了空表单'
        data = Picture.objects.filter(picture_user=request.user)
        girl_table = Picture.objects.filter(picture_user=request.user,picture_label="美女")
        boy_table = Picture.objects.filter(picture_user=request.user,picture_label="帅哥")
        flower_table = Picture.objects.filter(picture_user=request.user,picture_label="花")
        animal_table = Picture.objects.filter(picture_user=request.user,picture_label="动物")
        return render(request, 'index.html', {'girl': girl_table,'boy':boy_table,'flower':flower_table,'animal':animal_table})
    posts = Picture.objects.filter(picture_user=request.user)
    if "美女" in message:
        data = Picture.objects.filter(picture_user=request.user, picture_label="美女")
        return render(request,'index.html',{'girl':data,'base':posts})
    elif "帅哥" in message:
        data = Picture.objects.filter(picture_user=request.user, picture_label="帅哥")
        return render(request,'index.html',{'boy':data,'base':posts})
    elif "花" in message:
        data = Picture.objects.filter(picture_user=request.user, picture_label="花")
        return render(request,'index.html',{'flower':data,'base':posts})
    elif "动物" in message:
        data = Picture.objects.filter(picture_user=request.user, picture_label="动物")
        return render(request,'index.html',{'animal':data,'base':posts})
    else:
        data = Picture.objects.filter(picture_user=request.user)
        flag = 0
        for var in data:
            if message == var.picture_name:
                string = Get_pic_label(var.picture_label)
                data = Picture.objects.filter(picture_user=request.user,picture_name = message)
                return render(request,'index.html',{string:data,'base':posts})
            elif message in var.picture_name or var.picture_name in message:
                flag = 1
                string = var.picture_name
                stringlocation = Get_pic_label(var.picture_label)
        if flag == 1:
            data = Picture.objects.filter(picture_user = request.user,picture_name = string)
            return render(request,'index.html',{stringlocation:data,'base':posts})
        elif flag ==0:
            girl_table = Picture.objects.filter(picture_user=request.user,picture_label="美女")
            boy_table = Picture.objects.filter(picture_user=request.user,picture_label="帅哥")
            flower_table = Picture.objects.filter(picture_user=request.user,picture_label="花")
            animal_table = Picture.objects.filter(picture_user=request.user,picture_label="动物")
            return render(request, 'index.html', {'girl': girl_table,'boy':boy_table,'flower':flower_table,'animal':animal_table,'base':posts})
	    
