from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth.forms import UserCreationForm
from .form import PersonaForm
from .models import  Persona



# Create your views here.

def welcome(request):

    if request.user.is_authenticated:
        return render(request, "welcome.html")
    return redirect('/login')

def register(request):
    form = UserCreationForm
    if request.method == "POST":
        form = UserCreationForm(date=request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                do_login(request,user)
                return redirect('/')
    return render(request, "register.html", {'form':form})

def login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                do_login(request, user)
                return HttpResponseRedirect('/')
    return render(request, "login.html", {'form':form})

def logout(request):

    do_logout(request)

    return HttpResponseRedirect('/')


def add(request):
    form = PersonaForm()

    if request.method == "POST":
        form = PersonaForm(request.POST)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()
            return redirect('/')
    return render(request, "welcome.html",{'form':form})

def edit(request, persona_id):
    instancia = Persona.objects.get(id=persona_id)

    form = PersonaForm(instance=instancia)

    if request.method == "POST":
        form = PersonaForm(request.POST, instance=instancia)

        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()

    return render(request, "welcome.html",{'form':form})

def delete(request, persona_id):
    instancia = Persona.objects.get(id=persona_id)
    instancia.delete()

    return redirect('welcome')

def person(request):
    personas = Persona.objects.all()
    edad = 0

    if request.POST.get('edad'):
        edad = int(request.POST.get('edad'))
        personas = personas.filter(edad__get=edad)

    return(request, "welcome.html",{'personas':personas})