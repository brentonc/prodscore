from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django import forms
from django.template import RequestContext, loader
from todo.models import Task
from django.forms import ModelForm


class IndexView(generic.ListView):
    template_name = 'todo/index.html'
    context_object_name = 'tasks_list'

    def get_queryset(self):
        return Task.objects.all()


class DetailView(generic.DetailView):
    model = Task
    template_name = "todo/detail.html"


def detail(request, task_id):
    t = get_object_or_404(Task, pk=task_id)
    form = TodoForm(instance=t)
    return render(request, 'todo/detail.html', {
        'form': form,
    })


def new(request):
    form = TodoForm()


#def new(request):
    #if request.method == 'POST':
        #form = TodoForm(request.POST)
        #if form.is_valid():
            #t = Task()
            #t.title = form.cleaned_data['title']
            #t.description = form.cleaned_data['description']
            #t.value = form.cleaned_data['value']

            #return HttpResponseRedirect('/')
    #else:
        #form = TodoForm()

    #return render(request, 'todo/detail.html')


class TodoForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'value']
