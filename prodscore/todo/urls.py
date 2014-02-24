from django.conf.urls import patterns, url
from todo import views

urlpatterns = patterns('',
    #ex: /
    url(r'^$', views.IndexView.as_view(), name='index'),

    #ex:/5/
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
)
