from django.urls import path
from . import views


app_name = "project"
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:project_title>/show", views.show, name="show"),
    path("create/", views.create, name="create"),
    path("<str:project_title>/update", views.update, name="update"),
    path("<str:project_title>/delete", views.delete, name="delete"),
]
