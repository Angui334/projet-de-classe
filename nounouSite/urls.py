"""
URL configuration for nounouSite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog.views import inscription,connexion,accueil,Sophie,Alice,Pamela,Lohoues,Sarah,Latifa,deconnexion,formulaire_enfants
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',accueil,name="accueil"),
    path('blog/connexion',connexion,name="connexion"),
    path('blog/inscription',inscription,name="inscription"),
    path('blog/deconnexion',deconnexion,name="deconnexion"),
    path('blog/Sophie',Sophie,name="Sophie"),
    path('blog/Alice',Alice,name="Alice"),
    path('blog/pamela',Pamela,name="Pamela"),
    path('blog/Lohoues',Lohoues,name="Lohoues"),
    path('blog/Sarah',Sarah,name="Sarah"),
    path('blog/Latifa',Latifa,name="Latifa"),
    path('blog/Formulaire',formulaire_enfants,name="Formulaire")
]

