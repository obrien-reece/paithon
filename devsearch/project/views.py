from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm


def index(request):
    return render(request, "project/index.html", {
        "projects": Project.objects.all()
    })


def show(request, project_title):
    project = Project.objects.get(title=project_title)
    tags = project.tags.all()
    context = {"project": project, "tags": tags}
    return render(request, "project/show.html", context)


def create(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("project:index")

    context = {"form": form}
    return render(request, "project/project_form.html", context)


def update(request, project_title):
    project = Project.objects.get(title=project_title)
    form = ProjectForm(instance=project)
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        form.save()
        return redirect("project:index")

    context = {"form": form}
    return render(request, "project/project_form.html", context)


def delete(request, project_title):
    project = Project.objects.get(title=project_title)
    if request.method == "POST":
        project.delete()
        return redirect("project:index")

    context = {"project": project}
    return render(request, "project/delete.html", context)
