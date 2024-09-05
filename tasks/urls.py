"""
URL configuration for todo_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('create',views.createTask,name='create_tasks'),
    path('list',views.getTask,name='list_tasks'),
    path('delete/<int:task_id>/', views.deleteTaskById, name='delete_tasks_by_id'),
    path('delete-all', views.deleteAllTasks, name='delete_all_tasks'),
    path('update-state', views.updateTasksState, name='update_tasks_state'),
    path('edit/<int:task_id>/', views.editTaskById, name='edit_task_by_id'),

]