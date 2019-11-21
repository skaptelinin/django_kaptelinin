from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template.response import TemplateResponse
import random
from .models import TodoItem

todos = []
task = TodoItem()

def new_task(request):
    if request.method == 'POST':
        task.text = request.POST("text")
        task.status = request.POST("status")
        task.indentificator = request.POST("id")
        task.save()
    todos.append(task)
    return todos


def index(request):
    header = new_task(request)
    user = {'name': "Alex", 'age': 15}
    task = TodoItem()
    data = {'head': header, 'customer': user, 'task': task}
    return TemplateResponse(request, "index.html", context=data)

















def about(request):
    return HttpResponse("<h1>We are fraction FRACTION</h1>")

def adress(request):
    numb = request.GET.get("numb", "")
    name = request.GET.get("name", "")
    output = "<h1>Number {0}, Name {1}</h1>".format(numb, name)
    return HttpResponse(output)