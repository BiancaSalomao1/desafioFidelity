from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegistrarForm
from .models import Usuario
from django.contrib.auth.hashers import make_password
from contas.models import Usuario

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            usuario = authenticate(request, username=email, password=senha)
            if usuario is not None:
                login(request, usuario)
                return redirect('menu')
            else:
                try:
                    usuario = Usuario.objects.get(email=email)
                    messages.error(request, 'Senha inválida.')
                except Usuario.DoesNotExist:
                    messages.error(request, 'E-mail inexistente.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def registrar_view(request):
    if request.method == 'POST':
        form = RegistrarForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            senha = make_password(form.cleaned_data['senha'])
            Usuario.objects.create(nome=nome, email=email, senha=senha)
            messages.success(request, 'Registro realizado com sucesso!')
            return redirect('login')  # Redireciona para a página de login após o registro
    else:
        form = RegistrarForm()
    return render(request, 'registrar.html', {'form': form})