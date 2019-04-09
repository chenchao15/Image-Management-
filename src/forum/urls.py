from django.conf.urls import url
from . import views, auth_view,search,showimages,handleimage
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

	url(r'^index$', views.index, name = 'index'),
        
	#auth
	url(r'^login$', auth_view.login, name = 'login'),
	url(r'^authenticate$', auth_view.authenticate, name = 'authenticate'),
	url(r'^signup$', auth_view.signup, name = 'signup'),
	url(r'^signup/submit$', auth_view.signup_submit, name = 'signup-submit'),
	url(r'^logout$', auth_view.logout, name = 'logout'),

	url(r'^create$', views.create, name = 'create'),
        url(r'^search$', search.datasearch,name = 'search'),
        url(r'^showimage/([1-9][0-9]*)$', showimages.showimage,name = 'showimage'),
        url(r'^gausssmoothing$', handleimage.Gauss_smoothing,name = 'gausssmoothing'),
        url(r'^two_val_change$', handleimage.Two_val_change,name = 'two_val_change'),
        url(r'^grayscale$', handleimage.Grayscale,name = 'grayscale'),
        url(r'^image_rotating/([1-9][0-9]*)/([0-9]*)$', handleimage.Image_rotating,name = 'image_rotating'),
        url(r'^image_shrink$', handleimage.Image_shrink,name = 'image_shrink'),

	url(r'^post/([1-9][0-9]*)$', views.post, name = 'post'),
	url(r'^post/([1-9][0-9]*)/reply$', views.reply, name = 'reply'),
	url(r'^create/done/$', views.result, name = 'create_done'),

        url(r'^mypage$', views.mypage, name = 'mypage'),
        url(r'^myfriendpage/([1-9][0-9]*)$', views.myfriendpage, name = 'myfriendpage'),
        url(r'^$', views.picwall, name = 'picwall'),

        url(r'^base$', views.base, name = 'base'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
