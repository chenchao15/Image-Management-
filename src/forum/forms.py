from django import forms
from .models import Picture, Reply
from django.utils import timezone


class PostForm(forms.Form):
    #picture_user = forms.ForeignKey('auth.User')
    picture_load = forms.FileField()
    picture_name = forms.CharField()
    picture_label = forms.CharField()
    picture_message = forms.CharField()
    picture_time = forms.DateTimeField(initial=timezone.now)

	# class Meta:
	# 	model = Picture

	# 	fields = ('picture_user',  'picture_name', 'picture_load', 'picture_label', 'picture_message', 'picture_time')
#'picture_load',   , 'picture_time'   , 'picture_message'
class ReplyForm(forms.ModelForm):
	class Meta:
		model = Reply
		fields = ('content',)

