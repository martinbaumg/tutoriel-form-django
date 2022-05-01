from django.db import models 

class Arbre(models.Model):
	nom = models.CharField(max_length=30)
	date_vu = models.DateField(blank=True)
	localisation = models.CharField(max_length=30)