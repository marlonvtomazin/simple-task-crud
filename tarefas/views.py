from django.shortcuts import render, redirect, get_object_or_404
from .forms import TarefaForm
from .models import TarefaModel
from django.http import HttpRequest
# Create your views here.

def tarefas_home(request):
    contexto = {
        "nome": "Marlon",
        #envia todos registros das tarefas
        "tarefas": TarefaModel.objects.all()
    }
    return render(request, 'tarefas/home.html', contexto)

def tarefas_adicionar(request:HttpRequest):
    if request.method == "POST":
        #obtem os dados do form post
        formulario = TarefaForm(request.POST)
        #verifica se é valido
        if formulario.is_valid():
            #salva no banco
            formulario.save()
            #redireciona pra home conforme o name na url.py
            return redirect("tarefas:home")

    contexto = {
        'form': TarefaForm
    }
    return render(request, 'tarefas/adicionar.html', contexto)

def tarefas_remover(request:HttpRequest, id):
    tarefa = get_object_or_404(TarefaModel, id=id)
    tarefa.delete()
    return redirect("tarefas:home")

def tarefas_editar(request:HttpRequest, id):
    tarefa = get_object_or_404(TarefaModel, id=id)
    if request.method == "POST":
        #o formulario recebe os dados que o usuario inseriu e o instance que diz qual dado tá representando
        formulario = TarefaForm(request.POST, instance=tarefa)
        if formulario.is_valid():
            formulario.save()
            return redirect("tarefas:home")
    #cria um form novo porém ele já vem com os dados inseridos conforme o ID
    formulario = TarefaForm(instance=tarefa)
    context = {
        'form': formulario
    }
    return render(request, 'tarefas/editar.html', context)
