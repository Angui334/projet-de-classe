from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import Inscription,LoginForm,enfants
from . import forms
from blog.models import nounou,Competence
def accueil(request):
    Nounou=nounou.objects.all()
    return render(request ,'page_home.html',{'nounou':Nounou})

def connexion(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                message = f'Bonjour, {user.username}! Vous êtes connecté.'
                return redirect("accueil")
            else:
                message = 'Identifiants ou mot de passeinvalides.'
    return render(
        request, 'connexion.html', context={'form': form, 'message': message})

def inscription(request):
    if request.method=="POST":
        form=Inscription(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=Inscription()   
    return render(request ,'inscription.html',{'form':form})

def deconnexion(request):
    logout(request)  
    return redirect('accueil')


def Sophie(request):
    Nounou=nounou.objects.all()
    return render(request ,'Sophie.html',{'nounou':Nounou})

def Alice(request):
    Nounou=nounou.objects.all()
    return render(request ,'Alice.html',{'nounou':Nounou})

def Lohoues(request):
    Nounou=nounou.objects.all()
    return render(request ,'Lohoues.html',{'nounou':Nounou})

def Pamela(request):
    Nounou=nounou.objects.all()
    return render(request ,'Pamela.html',{'nounou':Nounou})

def Sarah(request):
    Nounou=nounou.objects.all()
    return render(request ,'Sarah.html',{'nounou':Nounou})

def Latifa(request):
    Nounou=nounou.objects.all()
    return render(request ,'Latifa.html',{'nounou':Nounou})

def formulaire_enfants(request):
    if request.method=="POST":
        form=enfants(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accueil')
    else:      
        form=enfants()
    return render(request ,'formulaire.html',{'form':form})
