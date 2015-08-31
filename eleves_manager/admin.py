from django.contrib import admin
from .models import Eleve, Classe, Annee, Section

# Register your models here.



class EleveAdmin(admin.ModelAdmin):
    list_display = ('nom_elv', 'pnom_elv', 'mail_elv', 'classe_elv')

admin.site.register(Annee)
admin.site.register(Eleve,EleveAdmin)
admin.site.register(Classe)
admin.site.register(Section)
