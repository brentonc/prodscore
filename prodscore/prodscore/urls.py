from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'prodscore.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^todo/', include('todo.urls', namespace="todo")),
    url(r'^admin/', include(admin.site.urls)),

)
