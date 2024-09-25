from django.urls import path

from todolist.views import (
    TodoCreateView,
    TodoListView,
    TodoDeleteView,
    TodoUpdateView,
    TagListView,
    TagUpdateView,
    TagDeleteView,
    TagCreateView
)

app_name = 'todolist'

urlpatterns = [
    path('', TodoListView.as_view(), name='home'),
    path('todo/', TodoListView.as_view(), name='todo-list'),
    path('todo/create/', TodoCreateView.as_view(), name='todo-create'),
    path('todo/<int:pk>/update/', TodoUpdateView.as_view(), name='todo-update'),
    path('todo/<int:pk>/delete/', TodoDeleteView.as_view(), name='todo-delete'),
    path('tag/', TagListView.as_view(), name='tag-list'),
    path('tag/create/', TagCreateView.as_view(), name='tag-create'),
    path('tag/<int:pk>/update/', TagUpdateView.as_view(), name='tag-update'),
    path('tag/<int:pk>/delete/', TagDeleteView.as_view(), name='tag-delete'),
]
