from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse


class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")


def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "Diary/index.html", {"tasks": request.session["tasks"]})


def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("Diary:index"))
        else:
            return render(request, "Diary/add.html", {"form": form})
    return render(request, "Diary/add.html", {"form": NewTaskForm()})

