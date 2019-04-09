from django.shortcuts import render, get_object_or_404, redirect
from .models import Picture, Reply
from .forms import PostForm, ReplyForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect
from django.http import HttpResponse

def Gauss_smoothing(request):
    return HttpResponse("Gauss_smoothing")

def Two_val_change(request):
    return HttpResponse("Two_val_change")

def Grayscale(request):
    return HttpResponse("Grayscale")

def Image_rotating(request,image_id,rotating_count):
    if rotating_count=="":
        rotating_count = "0";
    image = get_object_or_404(Picture, pk = image_id)
    cot = int(rotating_count)+1
    if cot == 4:
        cot = 0
    cot = str(cot)
    return render(request, 'showimage.html', {'showimage': image,"ccc":cot})

def Image_shrink(request):
    return HttpResponse("Image_shrink")
