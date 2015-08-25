# -*- coding: utf-8 -*-
from django.shortcuts import render

def home(request):
    return render(request, "pass_teck/index.html", {})
