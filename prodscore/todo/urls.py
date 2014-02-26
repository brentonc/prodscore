from django.conf.urls import patterns, url
from todo import views

urlpatterns = patterns('',
    #ex: /
    url(r'^$', views.IndexView.as_view(), name='index'),

    #ex:/5/
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    #url(r'^(?P<task_id>\d+)/$', views.detail, name='detail'),

    #ex:/new/
    #url(r'^new/$', views.create_a_task, name='new'),
    url(r'^new/$', views.CreateView.as_view(), name='new'),

)
