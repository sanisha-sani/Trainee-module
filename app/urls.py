from . import views
from django.views.generic import TemplateView
from django.urls import path, re_path
urlpatterns = [
    re_path(r'^$', views.trainee_index,name='trainee_index'),  
    re_path(r'^trainee_topic$', views.trainee_topic, name='trainee_topic'),
    re_path(r'^trainee_currentTopic$', views.trainee_currentTopic, name='trainee_currentTopic'),
    re_path(r'^trainee_previousTopic$', views.trainee_previousTopic, name='trainee_previousTopic'),

]   