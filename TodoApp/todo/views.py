from django.shortcuts import render, redirect
from .forms import todoForm
from .models import Day, Todo


def index(request):
    days = Day.objects.all()
    context = {"days": days}
    return render(request, "todo/index.html", context)


def create(request):
    form = todoForm()
    days = Day.objects.all()
    if request.method == "POST":
        form = todoForm(request.POST)
        if form.is_valid():
            selected_day = form.cleaned_data['day_id']  # Get the selected day
            new_todo = form.save(commit=False)  # Create a new Todo instance
            new_todo.day = selected_day  # Associate the selected day
            new_todo.save()  # Save the new Todo instance
            return redirect("todo:index")

    context = {
        "form": form,
        "days": days
    }
    return render(request, "todo/create_update.html", context)


def daycreate(request, weekday):
    weekday = Day.objects.get(day=weekday)
    initial_data = {"day_id": weekday.id}
    form = todoForm(initial=initial_data)
    context = {"form": form}
    return render(request, "todo/create_update.html", context)


def show(request, weekday):
    day = Day.objects.get(day=weekday)
    context = {"day": day}
    return render(request, "todo/show.html", context)


def update(request, todo_id):
    todo_item = Todo.objects.get(pk=todo_id)
    initial_data = {"day_id": todo_item.day.id}

    if request.method == "POST":
        form = todoForm(request.POST, instance=todo_item)
        if form.is_valid():
            form.instance.day = form.cleaned_data['day_id']
            form.save()
            return redirect("todo:index")
    form = todoForm(instance=todo_item, initial=initial_data)
    context = {"form": form}
    return render(request, "todo/create_update.html", context)
