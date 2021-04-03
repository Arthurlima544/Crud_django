from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import *
from . forms import *

# Queries são métodos para gerenciar os dados dos models -> isso só é possivel pq o django ao criar um model cria tbm uma api 
def index(request):
    tasks = Task.objects.all() #Queryset
    form = TaskForm() # instância de uma classe taskform (de um formulario)

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'tasks':tasks,'form':form}
    return render(request,'tasks/list.html',context) # retorna a renderização do bagui

def updateTask(request,pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance = task)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'form':form}

    return render(request,'tasks/update_task.html',context)

def deleteTask(request,pk):
    item = Task.objects.get(id=pk)
    context = {'item':item}
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    return render(request,'tasks/delete.html',context)
