from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.response import TemplateResponse
import random
from django.db import models
from .models import TodoItem
from .forms import TodoInputForm
from django.views.decorators.http import require_POST   

def index(request):
    todo_list = TodoItem.objects.order_by('id')
    input_form = TodoInputForm()
    data = {'form': input_form, 'todo_list': todo_list}
    return TemplateResponse(request, "index.html", context=data)

def completeTodo(request, todo_id):
    task = TodoItem.objects.get(pk = todo_id)
    task.status = TodoInputForm(request.GET['status'])
    task.save()
    return redirect('index')

@require_POST
def addTodo(request):
    input_form = TodoInputForm(request.POST)
    task = TodoItem(text = request.POST['text'])
    task.save()
    return redirect('index')



















# def about(request):
#     return HttpResponse("<h1>We are fraction FRACTION</h1>")

# def adress(request):
#     numb = request.GET.get("numb", "")
#     name = request.GET.get("name", "")
#     output = "<h1>Number {0}, Name {1}</h1>".format(numb, name)
#     return HttpResponse(output)