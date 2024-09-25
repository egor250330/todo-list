from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from todolist.forms import TagForm, TaskForm
from todolist.models import Task, Tag


class TodoListView(generic.ListView):
    model = Task
    template_name = 'todolist/todolist.html'
    context_object_name = 'todo_list'
    paginate_by = 10


class TodoCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "todolist/form.html"

    def get_success_url(self):
        return reverse_lazy("todolist:todo-list")


class TodoUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "todolist/form.html"

    def get_success_url(self):
        return reverse_lazy("todolist:todo-list")


class TodoDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todolist:todo-list")
    template_name = "todolist/todo_config_delete.html"


class TagListView(generic.ListView):
    model = Tag
    template_name = "todolist/taglist.html"
    context_object_name = 'tag_list'
    paginate_by = 5


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    template_name = "todolist/form.html"

    def get_success_url(self):
        return reverse_lazy("todolist:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    template_name = "todolist/form.html"

    def get_success_url(self):
        return reverse_lazy("todolist:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todolist:tag-list")
    template_name = "todolist/tag_config_delete.html"
