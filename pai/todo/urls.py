from . import views
from django.urls import path


app_name = "todo"
urlpatterns = [
   path("", views.index, name="index"),
   path("<str:weekday>/create", views.create, name="create"),
   path("<str:weekday>/store", views.store, name="store"),
]
