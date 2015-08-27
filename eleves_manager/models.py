import datetime

from django.db import models
from django.utils import timezone

# Create your models here.


"""class Section(models.Model):
    nom_section = models.CharField("Section", max_length=50)

    def __str__(self):
        return self.nom_section

class Annee(models.Model):
    nom_annee = models.CharField("Année", max_length=8)
    #s_annee = models.ManyToManyField(Section)
    def __str__(self):
        return self.nom_annee"""

class Eleve(models.Model) :
    nom_elv = models.CharField("nom de l'élève", max_length=30)
    pnom_elv = models.CharField("prénom de l'élève", max_length=30)
    dnaiss_elv = models.DateField('date de naissance', blank=True, null=True)
    mail_elv = models.EmailField('adresse mail', max_length=254, blank=True, null=True)
    #annee_elv = models.ForeignKey(Annee)

    def __str__(self):
        txt = self.pnom_elv + ' ' + self.nom_elv
        return txt
