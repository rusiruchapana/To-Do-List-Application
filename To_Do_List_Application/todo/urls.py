from django.urls import path
from . import views


urlpatterns = [
    path('tasks/create/', views.task_create),
    path('tasks/getAll/', views.task_list),
    path('tasks/getOneTask/<int:pk>/', views.task_detail),
    path('tasks/updateTask/<int:pk>/', views.task_update)
]
