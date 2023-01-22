from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth import authenticate,login,logout

def cadastro(request):
    if request.user.is_authenticated:
        return redirect('/divulgar/novo_pet')
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        comfirmar_senha = request.POST.get('confirmar_senha')

    if len(nome.strip()) == 0 or len(email.strip()) == 0:
        messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
        return render(request,'cadastro.html')
    if len(senha) < 8 or len(comfirmar_senha) <8:
        messages.add_message(request, constants.ERROR, 'A senha deve ter no minimo 8 caracteres')
        return render(request,'cadastro.html')
    if senha != comfirmar_senha:
         messages.add_message(request, constants.ERROR, 'As senhas não estão indenticas')
         return render(request,'cadastro.html')


    try:
        user = User.objects.create_user(
            username=nome, email=email, password=senha
        )
        messages.add_message(request, constants.SUCCESS, 'Usuario criado com sucesso ')
        return render(request,'cadastro.html')
        #sucesso
    except:
        #erro
        messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
        return render(request,'cadastro.html')
        
def logar(request):
    if request.user.is_authenticated:
        return redirect('/divulgar/novo_pet')
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        user = authenticate(username=nome, password=senha)
        if user is not None:
            login(request,user)
            return redirect('/divulgar/novo_pet')
        else:
          messages.add_message(request, constants.ERROR, 'Usuario não existe ')
          return render(request, 'login.html')
def sair(request):
    logout(request)
    return redirect('/auth/login')
