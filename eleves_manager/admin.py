from django.contrib import admin
from .models import Eleve

# Register your models here.



class EleveAdmin(admin.ModelAdmin):
    list_display = ('nom_elv', 'pnom_elv', 'mail_elv' )

#class SectionAdmin(admin.ModelAdmin):


admin.site.register(Eleve,EleveAdmin)
#admin.site.register(Section)
#admin.site.register(Annee)
