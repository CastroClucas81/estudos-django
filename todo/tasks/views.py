from django.core import paginator
from django.http.response import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404, redirect
from django.http import HttpResponse
#biblioteca mensagens
from django.contrib import messages
#paginacao
from django.core.paginator import Paginator

from .models import Task
# importando form de forms
from .forms import TaskForm

# Create your views here.
# definindo minha view como funcao


def helloWorld(request):
    return HttpResponse("helloWorld")


def taskList(request):
    #parâmetro get do campo de pesquisa search = name
    search = request.GET.get('search')

    if search:
        #ignora...
        tasks = Task.objects.filter(title__icontains=search)
    else:
        # pegar todas as tasks do bd e mandar pro front
        tasks_list = Task.objects.all().order_by('-created_at')

        #chamadno paginator
        paginator = Paginator(tasks_list, 3)
        page = request.GET.get('page')

        tasks = paginator.get_page(page)

    # recebe sempre dois parâmetros
    return render(request, 'tasks/list.html', {'tasks': tasks})


def yourName(request, name):
    return render(request, 'tasks/yourname.html', {'name': name})


def taskView(request, id):
    # se o id (pk) não existir retorna um 404
    task = get_object_or_404(Task, pk=id)
    return render(request, 'tasks/task.html', {'task': task})


def newTask(request):
    if request.method == "POST":
        # preenchendo os formulários com os dados do form
        form = TaskForm(request.POST)

        if form.is_valid():
            # vai parar o processo de insercao de dados e esperar até a gente falar
            task = form.save(commit=False)
            task.done = 'doing'
            task.save()
            return redirect('/')

    else:
        form = TaskForm()
        return render(request, 'tasks/addtask.html', {'form': form})


def editTask(request, id):
    task = get_object_or_404(Task, pk=id)

    # isso ajuda a deixar o formulário pré populado
    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            # vai parar o processo de insercao de dados e esperar até a gente falar
            task.save()
            return redirect('/')
        else:
            return render(request, 'tasks/edittask.html', {'form': form, 'task': task})

    else:
        return render(request, 'tasks/edittask.html', {'form': form, 'task': task})

def deleteTask(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()
    messages.info(request, "Tarefa deletada com sucesso!")

    return redirect('/')