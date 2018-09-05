from django.conf.urls import url,include
from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
    url(r'^like/?(?P<id>[0-9]+)', views.like, name='like'),
    url(r'^dislike/?(?P<id>[0-9]+)', views.dislike, name='dislike'),


    
    

    

]