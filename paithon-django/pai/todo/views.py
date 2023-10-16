from django.shortcuts import render
from django.http import HttpResponse
from .models import Day


def index(request):
    day_of_week = Day.objects.all()
    reminders = {}

    for dow in day_of_week:
        reminders[dow] = list(dow.reminder_set.all())

    return render(request, "todo/index.html", {
        "weekdays": day_of_week,
        "reminders": reminders
    })


def create(request, weekday):
    return render(request, "todo/create.html", {"weekday": weekday})


def store(request, weekday):
    return HttpResponse(weekday)
