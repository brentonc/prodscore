from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.template import RequestContext, loader
from todo.models import Task


class IndexView(generic.ListView):
    template_name = 'todo/index.html'
    context_object_name = 'tasks_list'

    def get_queryset(self):
        return Task.objects.all()


class DetailView(generic.DetailView):
    model = Task
    template_name = "todo/detail.html"
