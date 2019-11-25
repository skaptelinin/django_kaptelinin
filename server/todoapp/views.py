from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.db import models
from .models import TodoItem
from .forms import TodoInputForm
from .forms import TodoEditForm
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import re 

todo_selector = 'show all tasks'

page = 1
paginator = Paginator(TodoItem.objects.all(), 5)

def todoRender():
    if todo_selector == 'show all tasks':
        return TodoItem.objects.order_by('id')
    if todo_selector == 'show completed tasks':
        return TodoItem.objects.filter(status = True).order_by('id')
    if todo_selector == 'show tasks in progress':
        return TodoItem.objects.filter(status = False).order_by('id')

def index(request):
    global todo_selector
    global page
    todo_list_adaptive = todoRender()
    input_form = TodoInputForm()
    todo_status = TodoItem.status
    todo_completed = TodoItem.objects.filter(status = True).count()
    todo_in_progress = TodoItem.objects.filter(status = False).count()
    paginator = Paginator(todo_list_adaptive, 5)
    try:
        todos = paginator.page(page)
    except PageNotAnInteger:
        todos = paginator.page(1)
    except EmptyPage:
        todos = paginator.page(paginator.num_pages)
    data = {'form': input_form, 
        'todo_list': todos,
        'todo_status': todo_status,
        'completed': todo_completed,
        'in_progress': todo_in_progress,
        'selector': todo_selector, 
    }

    return TemplateResponse(request, "index.html", context=data)

@require_POST
def addTodo(request):
    global page
    page = TodoItem.objects.all().count()+1
    global todo_selector
    todo_selector = 'show all tasks'
    input_form = request.POST['text'].strip()
    if len(input_form):
        input_form = re.sub(r'\s+', ' ', input_form)
        task = TodoItem(text = input_form)
        task.save()

    return redirect('index')

def completeTodo(request, todo_id):
    task = TodoItem.objects.get(pk = todo_id)
    task.status = not task.status
    task.save()

    return redirect('index')

def deleteTodo(request, todo_id):
    # global page
    task = TodoItem.objects.get(pk = todo_id)
    task.delete()
    # page = paginator.num_pages

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
    global page
    todo_selector = 'show all tasks'
    page = 1

    return redirect('index')

def showCompleted(request):
    global todo_selector
    global page
    todo_selector = 'show completed tasks'
    page = 1

    return redirect('index')

def showInProgress(request):
    global todo_selector
    global page
    todo_selector = 'show tasks in progress'
    page = 1

    return redirect('index')

def editTodo(request, todo_id):
    task = TodoItem.objects.get(pk = todo_id)
    input_form = request.POST['edit-text'].strip()
    print('text is ', input_form)
    if len(input_form):
        input_form = re.sub(r'\s+', ' ', input_form)
        task.text = input_form
        task.save()

    return redirect('index')

def turnPage(request, page_number):
    global page
    page = page_number

    return redirect('index')

