from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('work', views.work, name="work"),
    path("place", views.place, name="place"),
    path("salary", views.salary, name="salary"),
    path("task", views.task, name="task"),
    path("frds", views.frds, name="frds"),
    path("college", views.college, name="college"),
]
