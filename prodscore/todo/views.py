from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django import forms
from django.template import RequestContext, loader
from django.forms import ModelForm
from todo.models import Task
from todo.forms import TodoForm


class IndexView(generic.ListView):
    template_name = 'todo/index.html'
    context_object_name = 'tasks_list'

    def get_queryset(self):
        return Task.objects.all()


class DetailView(generic.UpdateView):
    model = Task
    template_name = "todo/detail.html"
    form_class = TodoForm
    success_url = '/todo/'


class CreateView(generic.CreateView):
    model = Task
    template_name = "todo/detail.html"
    form_class = TodoForm
    success_url = '/todo/'


def create_a_task(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            t = form.save()
    else:
        form = TodoForm()
    c = {'form': form}

    return render(request, 'todo/detail.html', c)
