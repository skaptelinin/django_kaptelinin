from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.db import models
from .models import TodoItem
from .forms import TodoInputForm
from .forms import TodoEditForm
from django.views.decorators.http import require_POST   

todo_selector = 'show all tasks'

def todoRender():
    if todo_selector == 'show all tasks':
        return TodoItem.objects.order_by('id')
    if todo_selector == 'show completed tasks':
        return TodoItem.objects.filter(status = True).order_by('id')
    if todo_selector == 'show tasks in progress':
        return TodoItem.objects.filter(status = False).order_by('id')

def index(request):
    global todo_selector
    todo_list_adaptive = todoRender()
    input_form = TodoInputForm()
    todo_status = TodoItem.status
    todo_completed = TodoItem.objects.filter(status = True).count()
    todo_in_progress = TodoItem.objects.filter(status = False).count()
    data = {'form': input_form, 
        'todo_list': todo_list_adaptive,
        'todo_status': todo_status,
        'completed': todo_completed,
        'in_progress': todo_in_progress,
        'selector': todo_selector, 
    }

    return TemplateResponse(request, "index.html", context=data)

@require_POST
def addTodo(request):
    global todo_selector
    todo_selector = 'show all tasks'
    input_form = request.POST['text'].strip()
    if len(input_form):
        task = TodoItem(text = request.POST['text'])
        task.save()

    return redirect('index')

def completeTodo(request, todo_id):
    task = TodoItem.objects.get(pk = todo_id)
    task.status = not task.status
    task.save()

    return redirect('index')

def deleteTodo(request, todo_id):
    task = TodoItem.objects.get(pk = todo_id)
    task.delete()

    return redirect('index')

def deleteCompleted(request):
    TodoItem.objects.filter(status__exact = True).delete()
    
    return redirect('index')

def checkAll(request):
    if TodoItem.objects.filter(status = False).count():
        TodoItem.objects.all().update(status = True)
    else:
        TodoItem.objects.all().update(status = False)

    return redirect('index')

def showAll(request):
    global todo_selector
    todo_selector = 'show all tasks'

    return redirect('index')

def showCompleted(request):
    global todo_selector
    todo_selector = 'show completed tasks'

    return redirect('index')

def showInProgress(request):
    global todo_selector
    todo_selector = 'show tasks in progress'

    return redirect('index')

