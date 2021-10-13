from django import forms
from .models import Task

#no python cria class pra form
class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        #campos que eu quero q aparecam no front
        fields = ('title', 'description')