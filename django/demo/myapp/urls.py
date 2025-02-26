from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"), # call home function from views.py 
    path("todos/", views.todos, name="Todos")
]