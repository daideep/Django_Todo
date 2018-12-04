from django.shortcuts import render,HttpResponse,redirect
#from django.views.decorators.http import require_POST

from .models import Todo
from .form import TodoForm
import datetime

def index(request):

    todo_list = Todo.objects.order_by('id')

    Form = TodoForm()

    mydate = datetime.datetime.now()

    context = {'todo_list': todo_list, 'form' : Form, 'date' : mydate}

    return render(request, 'todo/index.html', context)
  # return HttpResponse("dffhggf")

#@require_POST
def addtodo(request):

    # form = TodoForm(request.POST)

    # if form.is_valid():
    add = Todo(list=request.POST['text'])
    add.save()

    return redirect('index')


def complete(request,t_id):
    todo = Todo.objects.get(id = t_id)
    todo.complete = True
    todo.save()

    return redirect('index')


def deletecomplete(request):

    Todo.objects.filter(complete__exact = True).delete()

    return redirect('index')


def deleteall(request):

    Todo.objects.all().delete()

    return redirect('index')

