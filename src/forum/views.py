from django.shortcuts import render, get_object_or_404, redirect
from .models import Picture, Reply
from .forms import PostForm, ReplyForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect
from django.http import HttpResponse
import random

from django.contrib.auth.models import User

def base(request):
        posts = Picture.objects.order_by('-picture_time').filter(picture_user=request.user)
        #return render(request, 'base.html', {'base': posts})
        return HttpResponse("ffff")

def index(request):
	posts = Picture.objects.filter(picture_user=request.user).order_by('-picture_time')
	friend = User.objects.all()
	girl_table = Picture.objects.filter(picture_user=request.user,picture_label="美女")
	boy_table = Picture.objects.filter(picture_user=request.user,picture_label="帅哥")
	flower_table = Picture.objects.filter(picture_user=request.user,picture_label="花")
	animal_table = Picture.objects.filter(picture_user=request.user,picture_label="动物")
	return render(request, 'index.html', {'girl': girl_table,'boy':boy_table,'flower':flower_table,'animal':animal_table,'base':posts,'friend':friend})

def mypage(request):
        posts = Picture.objects.filter(picture_user=request.user).order_by('-picture_time')
        return render(request, 'mypage.html',{'mypagePic':posts})

def myfriendpage(request,id):
        friend = User.objects.get(id = id)
        posts = Picture.objects.filter(picture_user=friend).order_by('-picture_time')
        return render(request, 'mypage.html',{'mypagePic':posts})


def picwall(request):
        all_pic = Picture.objects.all()
        new_pic = []
        for i in range(0,len(all_pic)):
                randompic_id = random.randint(0,len(all_pic)-1)
                new_pic.append(all_pic[randompic_id])
        return render(request, 'picwall.html',{'new_pic':new_pic})

@login_required
def create(request):
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)

		if form.is_valid():
			post = Picture()
			post.picture_user = request.user
			post.picture_name = form.cleaned_data['picture_name']
			post.picture_load = form.cleaned_data['picture_load']
			post.picture_message = form.cleaned_data['picture_message']
			post.picture_label = form.cleaned_data['picture_label']
			post.picture_time = form.cleaned_data['picture_time']
			post.save()
			request.session['photo_info'] = post.picture_name
			return HttpResponseRedirect('/create/done/')
	else:
		form = PostForm()
	return render(request, 'create.html', {'form':form})

def result(request):
	users = Picture.objects.all()
	content = { 'users':users }
	user = Picture.objects.get(picture_name = request.session['photo_info'])
	return HttpResponseRedirect('/')

def post(request, post_id):
	post = get_object_or_404(Picture, pk = post_id)
	reply_form = ReplyForm()
	return render(request, 'post.html', {'post': post, 'reply_form': reply_form})

@login_required
@require_POST
def reply(request, post_id):
	post = get_object_or_404(Picture, pk = post_id)
	form = ReplyForm(request.POST)
	if form.is_valid():
		reply = form.save(commit = False)
		reply.author = request.user
		reply.post = post
		reply.content = request.POST.get('content')
		print(reply.save())
		messages.info(request, ' 帖子《{}》回复成功'.format(post.title))
	else:
		print('not valid')
		messages.warning(request, ' 帖子《{}》回复失败')

	return redirect('post', post.id)
