# Creamos la vista aqui.
from principal.models import Receta
from django.shortcuts import render_to_response

def lista_recetas(request):
	recetas = Receta.objects.exclude(ingredientes__startswith='z')
	return render_to_response('lista_recetas.html',{'lista':recetas})