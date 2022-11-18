from django import forms
from django.shortcuts import render

task = ["foo", "bar", "baz"]

class NewTaskForm(forms.Form):
    tasks = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)

# Create your views here.
def index(request):
    return render(request, "task/index.html", {
        "task": task
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            tasks.append(task)
        else:
            return render(request, "task/add.html", {
                "form": form
            })
    return render(request, "task/add.html", {
        "form":NewTaskForm()
    })
