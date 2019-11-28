"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('addTodo', views.addTodo, name='addTodo'),
    path('checkTodo/<todo_id>', views.checkTodo, name='checkTodo'),
    path('uncheckTodo/<todo_id>', views.uncheckTodo, name='uncheckTodo'),
    path('deleteCompleted', views.deleteCompleted, name='deleteCompleted'),
    path('deleteTodo/<todo_id>', views.deleteTodo, name='deleteTodo'),
    path('checkAll', views.checkAll, name='checkAll'),
    path('uncheckAll', views.uncheckAll, name='uncheckAll'),
    path('showAll', views.showAll, name='showAll'),
    path('showCompleted', views.showCompleted, name='showCompleted'),
    path('showInProgress', views.showInProgress, name='showInProgress'),
    path('editTodo/<todo_id>', views.editTodo, name='editTodo'),
    path('turnPage/<page_number>', views.turnPage, name='turnPage'),
]
