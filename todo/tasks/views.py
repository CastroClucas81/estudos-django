from django.core import paginator
from django.http.response import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404, redirect
from django.http import HttpResponse
# biblioteca mensagens
from django.contrib import messages
# paginacao
from django.core.paginator import Paginator

from .models import Task
# importando form de forms
from .forms import TaskForm
import datetime

# login required
from django.contrib.auth.decorators import login_required

# Create your views here.
# definindo minha view como funcao


def helloWorld(request):
    return HttpResponse("helloWorld")


@login_required
def taskList(request):
    # parâmetro get do campo de pesquisa search = name
    search = request.GET.get('search')
    filter = request.GET.get('filter')

    #dashboard
    tasksDoneRecently = Task.objects.filter(
        done='done', updated_At__gt=datetime.datetime.now() - datetime.timedelta(days=30), user=request.user).count()
    tasksDone = Task.objects.filter(done='done', user=request.user).count()
    tasksDoing = Task.objects.filter(done='doing', user=request.user).count()

    if search:
        # request.user = usuário autenticado
        tasks = Task.objects.filter(title__icontains=search, user=request.user)

    elif filter:
        tasks = Task.objects.filter(done=filter, user=request.user)

    else:
        # pegar todas as tasks do bd e mandar pro front
        tasks_list = Task.objects.all().order_by(
            '-created_at').filter(user=request.user)

        # chamadno paginator
        paginator = Paginator(tasks_list, 3)
        page = request.GET.get('page')

        tasks = paginator.get_page(page)

    # recebe sempre dois parâmetros
    return render(request, 'tasks/list.html', {'tasks': tasks, 'tasksDoneRecently': tasksDoneRecently, 'tasksDone': tasksDone, 'tasksDoing': tasksDoing})


@login_required
def yourName(request, name):
    return render(request, 'tasks/yourname.html', {'name': name})


@login_required
def taskView(request, id):
    # se o id (pk) não existir retorna um 404
    task = get_object_or_404(Task, pk=id)
    return render(request, 'tasks/task.html', {'task': task})


@login_required
def newTask(request):
    if request.method == "POST":
        # preenchendo os formulários com os dados do form
        form = TaskForm(request.POST)

        if form.is_valid():
            # vai parar o processo de insercao de dados e esperar até a gente falar
            task = form.save(commit=False)
            task.done = 'doing'
            # passando o usuário
            task.user = request.user
            task.save()
            return redirect('/')

    else:
        form = TaskForm()
        return render(request, 'tasks/addtask.html', {'form': form})


@login_required
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


@login_required
def deleteTask(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()
    messages.info(request, "Tarefa deletada com sucesso!")

    return redirect('/')


@login_required
def changeStatus(required, id):
    task = get_object_or_404(Task, pk=id)

    if(task.done == 'doing'):
        task.done = 'done'
    else:
        task.done = 'doing'

    task.save()

    return redirect('/')
