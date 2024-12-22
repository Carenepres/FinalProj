import logging
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseBadRequest
from .models import Task
from .forms import TaskForm

# Create a logger
logger = logging.getLogger(__name__)

# Create your views here.
def task_list(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            logger.info("Task created successfully")
            return redirect("task-list")
        else:
            logger.warning("Invalid form submission")
            return HttpResponseBadRequest("Invalid data")
    context = {"tasks": tasks, "form": form}
    return render(request, "task_list.html", context)

def task_update(request, pk):
    task = get_object_or_404(Task, id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            logger.info(f"Task {pk} updated successfully")
            return redirect("task-list")
        else:
            logger.warning(f"Invalid form submission for task {pk}")
            return HttpResponseBadRequest("Invalid data")
    context = {"form": form}
    return render(request, "task_list.html", context)

def task_delete(request, pk):
    task = get_object_or_404(Task, id=pk)
    if request.method == 'POST':
        task.delete()
        logger.info(f"Task {pk} deleted successfully")
        return redirect("task-list")
    context = {"task": task}
    return render(request, "task_delete.html", context)