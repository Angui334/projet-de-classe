from django.db import models

class nounou(models.Model):
    nom=models.CharField(max_length=50)
    prenom=models.CharField(max_length=50)
    adresse=models.CharField(max_length=50)
    telephone=models.CharField(max_length=20)

class Competence(models.Model):
    nounou_competences=models.CharField(max_length=30,null=True)

class Tarif(models.Model):
    Nos_prix=models.CharField(max_length=10)

class Enfant(models.Model):
    Nom=models.CharField(max_length=70)
    Prenom=models.CharField(max_length=70)
    Date_naissance=models.DateField()
    Adresse=models.CharField(max_length=70)
    Competences=models.ForeignKey(Competence,on_delete=models.SET_NULL,null=True)
    Nounou=models.ManyToManyField(nounou)
    nombre_enfants=models.IntegerField()
    Description_enfants=models.TextField()
    Prix=models.ForeignKey(Tarif,on_delete=models.CASCADE)










