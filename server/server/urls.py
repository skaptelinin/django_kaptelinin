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
    path('add_todo', views.add_todo, name='add_todo'),
    path('check_todo/<todo_id>', views.check_todo, name='check_todo'),
    path('uncheck_todo/<todo_id>', views.uncheck_todo, name='uncheck_todo'),
    path('delete_completed', views.delete_completed, name='delete_completed'),
    path('delete_todo/<todo_id>', views.delete_todo, name='delete_todo'),
    path('check_all', views.check_all, name='check_all'),
    path('uncheck_all', views.uncheck_all, name='uncheck_all'),
    path('show_all', views.show_all, name='show_all'),
    path('show_completed', views.show_completed, name='show_completed'),
    path('show_in_progress', views.show_in_progress, name='show_in_progress'),
    path('edit_todo/<todo_id>', views.edit_todo, name='edit_todo'),
    path('turn_page/<page_number>', views.turn_page, name='turn_page'),
]
