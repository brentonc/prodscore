from django.forms import ModelForm
from todo.models import Task


class TodoForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'value']
