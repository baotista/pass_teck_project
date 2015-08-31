import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Section(models.Model) :
    nom_sec = models.CharField("section",max_length=30)
    def __str__(self) :
        return self.nom_sec

class Annee(models.Model) :
    num_an = models.IntegerField(default=0)
    nom_an =models.CharField("année",max_length=5)
    def __str__(self) :
        return self.nom_an

class Classe(models.Model) :
    nom_cls = models.CharField("classe",max_length=30)
    an_cls = models.ForeignKey(Annee)
    sec_cls = models.ForeignKey(Section)
    def __str__(self):
        return self.nom_cls

class Eleve(models.Model) :
    nom_elv = models.CharField("nom de l'élève", max_length=30)
    pnom_elv = models.CharField("prénom de l'élève", max_length=30)
    dnaiss_elv = models.DateField('date de naissance', blank=True, null=True)
    mail_elv = models.EmailField('adresse mail', max_length=254, blank=True, null=True)
    grp_elv = models.IntegerField(default=0)
    classe_elv = models.ForeignKey(Classe)

    def __str__(self):
        txt = self.pnom_elv + ' ' + self.nom_elv
        return txt
