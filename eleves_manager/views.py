from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Eleve
# Create your views here.


class IndexView(generic.ListView):
    template_name = 'eleves_manager/index.html'
    context_object_name = 'eleves_list'

    def get_queryset(self):
        """Retourne une liste d'élèves."""
        return Eleve.objects.order_by('-nom_elv')[:5]


class DetailView(generic.DetailView):
    model = Eleve
    template_name = 'eleves_manager/detail.html'
