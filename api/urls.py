from django.urls import path
from api.views import AddTodos, ListOfTodos 

urlpatterns = [
    path('todo-list/', ListOfTodos.as_view()),
    path('add-todo/', AddTodos.as_view())
]
