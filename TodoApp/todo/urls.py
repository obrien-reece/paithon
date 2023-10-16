from django.urls import path
from . import views


app_name = "todo"
urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("create/<str:weekday>/", views.daycreate, name="daycreate"),
    path("show/<str:weekday>/", views.show, name="show"),
    path("update/<str:todo_id>/", views.update, name="update"),
]
