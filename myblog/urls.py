from django.conf.urls import  url
from . import views
#from django_filters.views import FilterView
#from .filters import UserFilter

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/$', views.post, name='post'),
    url(r'^add/$', views.add, name='add'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^answer/(?P<pk>[0-9]+)/$', views.answer, name='answer'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^notifications$', views.notifications, name='notifications'),
    url(r'^password/$', views.change_password, name='change_password'),
    #filter urls 
    url(r'^math/$', views.math, name='math'),
    url(r'^physics/$', views.physics, name='physics'),
    url(r'^chemistry/$', views.chemistry, name='chemistry'),
    url(r'^entrepreneurship/$', views.entrepreneurship, name='entrepreneurship'),
    url(r'^computer/$', views.computer, name='computer'),
    url(r'^biology/$', views.biology, name='biology'),
    url(r'^literature/$', views.literature, name='literature'),
    url(r'^economics/$', views.economics, name='economics'),
    url(r'^history/$', views.history, name='history'),
    url(r'^geography/$', views.geography, name='geography'),
   
    url(r'^home/$', views.home, name='home'),
    url(r'^display_comment/$', views.display_comment, name='display_comment'),
    url(r'^comment/$', views.comment, name='comment'),
    url(r'^new/$', views.new, name='new'),
    
    url(r'^detail/$', views.detail, name='detail'),
    
    url(r'^answ(?P<album_id>[0-9]+)$', views.answ, name='answ'),

    #
    url(r'^project/$', views.project, name='project'),
    url(r'^teachers/$', views.teachers, name='teachers'),
    url(r'^post/(?P<pk_id>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),

    #project selection
    url(r'^science$', views.science, name='science'),
    url(r'^arts$', views.arts, name='arts'),
    url(r'^skills$', views.skills, name='skills'),

    #school
    url(r'^save_school$', views.save_school, name='save_school'),
    url(r'^model_form_upload$', views.model_form_upload, name='model_form_upload'),
    
    ]