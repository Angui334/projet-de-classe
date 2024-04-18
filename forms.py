from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from blog.models import Enfant
class Inscription(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={
        "class":"input",
        "type":"text",
        "placeholder":"Nom"
    }))

    email=forms.CharField(widget=forms.TextInput(attrs={
        "class":"input",
        "type":"email",
        "placeholder":"email"
    }))

    password1=forms.CharField(widget=forms.TextInput(attrs={
        "class":"input",
        "type":"password",
        "placeholder":"Mot de passe"
    }))

    password2=forms.CharField(widget=forms.TextInput(attrs={
        "class":"input",
        "type":"password",
        "placeholder":"Confirmation"
    }))

    class Meta:
        model=User
        fields=['username','email','password1','password2']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label='Nom d’utilisateur')
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Mot de passe')

class enfants(forms.ModelForm):
    Nom=forms.CharField(widget=forms.TextInput(attrs={
    
        "type":"text",
        "placeholder":"Nom",
        "class":"formbold-form-input"
    }))
    Prenom=forms.CharField(widget=forms.TextInput(attrs={
    
        "type":"text",
        "placeholder":"Konan",
        "class":"formbold-form-input"
    }))
    Date_naissance=forms.DateField(widget=forms.SelectDateWidget(years=range(1999,2024),attrs={
    
        "type":"date",
        "class":""
    }))

    Adresse=forms.CharField(widget=forms.TextInput(attrs={
    
        "type":"text",
        "placeholder":"Abidjan,Cocody,Riviera M'badon",
        "class":"formbold-form-input"
    }))
    nombre_enfants=forms.IntegerField(widget=forms.NumberInput(attrs={

        "type":"number",
        "placeholder":"0",
        "class":"formbold-form-input"
    }))
    Description_enfants=forms.CharField(widget=forms.Textarea(attrs={

        "type":"text",
        "placeholder":"La plus petite ama est beaucoup enthousiaste",
        "class":"formbold-form-input"
    }))


    class Meta:
        model=Enfant
        fields=['Nom','Prenom','Date_naissance','Adresse','Nounou','Competences','nombre_enfants','Description_enfants','Prix']
    