from django.shortcuts import render, get_object_or_404, redirect
from .models import Picture, Reply
from .forms import PostForm, ReplyForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect

def showimage(request,image_id):
    image = get_object_or_404(Picture, pk = image_id)
    return render(request, 'showimage.html', {'showimage': image})
