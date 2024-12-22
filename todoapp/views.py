from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseBadRequest
from .models import Task
from .forms import TaskForm

# Create your views here.
def task_list(request):
    tasks = Task.objects.all()
    form = TaskForm()
    custom_error_message = ""
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            if form.custom_error_message:
                custom_error_message = form.custom_error_message
            else:
                form.save()
                return redirect("task-list")
        else:
            custom_error_message = "Invalid data"
    context = {"tasks": tasks, "form": form, "custom_error_message": custom_error_message}
    return render(request, "task_list.html", context)

def task_update(request, pk):
    task = get_object_or_404(Task, id=pk)
    form = TaskForm(instance=task)
    custom_error_message = ""
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            if form.custom_error_message:
                custom_error_message = form.custom_error_message
            else:
                form.save()
                return redirect("task-list")
        else:
            custom_error_message = "Invalid data"
    context = {"form": form, "custom_error_message": custom_error_message}
    return render(request, "task_list.html", context)

def task_delete(request, pk):
    task = get_object_or_404(Task, id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect("task-list")
    context = {"task": task}
    return render(request, "task_delete.html", context)