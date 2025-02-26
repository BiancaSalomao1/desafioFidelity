from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .models import Usuario
from django.contrib import messages
from contas.models import Usuario

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')

def registrar(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        
        user = Usuario.objects.create_user(username=username, email=email, password=password)
        user.save()
        
        messages.success(request, "Registro bem-sucedido!")
        return redirect("login")

    return render(request, "registrar.html")

def logar(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        
        user = authenticate(request, username=email, password=password)
        
        if user:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Credenciais inválidas!")

    return render(request, "login.html")

def sair(request):
    logout(request)
    return redirect("login")
