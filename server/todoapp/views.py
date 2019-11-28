from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.template.response import TemplateResponse
from django.db import models
from .models import TodoItem
from .forms import TodoInputForm, TodoEditForm
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import re 

todo_selector = 'SHOW_ALL_TASKS'
page = 1

def get_todo_items():
    if todo_selector == 'SHOW_ALL_TASKS':
        return TodoItem.objects.order_by('id')
    if todo_selector == 'SHOW_COMPLETED_TASKS':
        return TodoItem.objects.filter(status=True).order_by('id')
    if todo_selector == 'SHOW_TASKS_IN_PROGRESS':
        return TodoItem.objects.filter(status=False).order_by('id')

def index(request):
    global todo_selector
    global page
    todo_list_adaptive = get_todo_items()
    input_form = TodoInputForm()
    edit_form = TodoEditForm()
    todo_status = TodoItem.status
    todo_completed = TodoItem.objects.filter(status=True).count()
    todo_in_progress = TodoItem.objects.filter(status=False).count()
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
        'edit_form': edit_form, 
    }
    return TemplateResponse(request, "index.html", context=data)

def error_message():
    h1row = '<h1>Oops! Something goes wrong.</h1>'
    h3row = '<h3>Try go back and reload todo page</h3>'
    return HttpResponse(h1row + h3row)

@require_POST
def add_todo(request):
    global page
    page = TodoItem.objects.all().count() + 1
    global todo_selector
    todo_selector = 'SHOW_ALL_TASKS'
    input_form = TodoInputForm(data=request.POST)
    if input_form.is_valid():
        Text = input_form.cleaned_data.get('text')
        task = TodoItem(text=Text)
        task.save()
    return redirect('index')

def check_todo(request, todo_id):
    try:
        task = TodoItem.objects.get(pk=todo_id)
        task.status = True
        task.save()
    except TodoItem.DoesNotExist:
        return error_message()
    return redirect('index')

def uncheck_todo(request, todo_id):
    try:
        task = TodoItem.objects.get(pk=todo_id)
        task.status = False
        task.save()
    except TodoItem.DoesNotExist:
        return error_message()
    return redirect('index')

def delete_todo(request, todo_id):
    try:
        task = TodoItem.objects.get(pk=todo_id)
        task.delete()
    except TodoItem.DoesNotExist:
        return error_message()
    return redirect('index')

def delete_completed(request):
    TodoItem.objects.filter(status=True).delete()    
    return redirect('index')

def check_all(request):
    TodoItem.objects.all().update(status=True)
    return redirect('index')

def uncheck_all(request):
    TodoItem.objects.all().update(status=False)
    return redirect('index')

def show_all(request):
    global todo_selector
    global page
    todo_selector = 'SHOW_ALL_TASKS'
    page = 1
    return redirect('index')

def show_completed(request):
    global todo_selector
    global page
    todo_selector = 'SHOW_COMPLETED_TASKS'
    page = 1
    return redirect('index')

def show_in_progress(request):
    global todo_selector
    global page
    todo_selector = 'SHOW_TASKS_IN_PROGRESS'
    page = 1
    return redirect('index')

def edit_todo(request, todo_id):
    try:
        task = TodoItem.objects.get(pk=todo_id)
        input_form = TodoEditForm(data=request.POST)
        if input_form.is_valid():
            Text = input_form.cleaned_data.get('text')
            task.text = Text
            task.save()
        
    except TodoItem.DoesNotExist:
        return error_message()
    return redirect('index')

def turn_page(request, page_number):
    global page
    page = page_number
    return redirect('index')

