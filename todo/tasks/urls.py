from django.urls import path

from . import views

''' CRIANDO URL HELLOWORLD
    é importante colocar o views. pra informar de onde está vindo
'''
urlpatterns = [
    path('helloworld/', views.helloWorld),
    path('', views.taskList, name='task-list'),
    path('task/<int:id>', views.taskView, name="task-view"),
    path('newtask/', views.newTask, name="new-task"),
    path('edittask/<int:id>', views.editTask, name="edit-task"),
    path('yourname/<str:name>', views.yourName, name='your-name')
]