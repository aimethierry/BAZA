from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.add, name='add'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^answer/(?P<pk>[0-9]+)/$', views.answer, name='answer'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^notifications$', views.notifications, name='notifications'),
    url(r'^password/$', views.change_password, name='change_password'),
    #filter urls 
    url(r'^chemistry$', views.chemistry, name='chemistry'),
    url(r'^math$', views.math, name='math'),
    url(r'^biology$', views.biology, name='biology'),
    url(r'^history$', views.history, name='history'),
    url(r'^economics$', views.economics, name='economics'),
    url(r'^geography$', views.geography, name='geography'),
    url(r'^literature$', views.literature, name='literature'),
    url(r'^entrepreneurship$', views.entrepreneurship, name='entrepreneurship'),
    url(r'^physics$', views.physics, name='physics'),
    url(r'^computer$', views.computer, name='computer'),
    
    ]