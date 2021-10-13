from django.db import models

# Create your models here.


class Task(models.Model):

    STATUS = (('doing', 'Fazendo'), ('done', 'Feito'))

    title = models.CharField(max_length=255)
    description = models.TextField()
    done = models.CharField(max_length=5, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_At = models.DateTimeField(auto_now=True)

    #mostrar o nome da tarefa no admin
    def __str__(self):
        return self.title

