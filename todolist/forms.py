from django import forms

from todolist.models import Task, Tag


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['content', 'deadline', 'is_done', 'tags']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
