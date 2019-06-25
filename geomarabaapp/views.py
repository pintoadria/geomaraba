from django.shortcuts import render, HttpResponseRedirect, render_to_response, get_object_or_404
from .models import Dados, Brand, Car, Nucleo, Bairro
import json

def principal(request):
    return render(request, 'geomaraba/principal.html', {})

def principal2(request):
	nucleo = Nucleo.objects.all()
	bairro = Bairro.objects.all()
	return render(request, 'geomaraba/principal2.html', locals())
	
def mapa(request):
    mapas = Dados.objects.all() 
    return render(request, 'geomaraba/mapa.html', {'mapas': mapas})
	
def regcar(request):
	if request.method == "POST":
		a = request.POST['drop1']
		return render(request, 'geomaraba/regcar.html', locals())
		#return HttpResponseRedirect('/carro/')
	
	brands = Nucleo.objects.all()
	cars = Bairro.objects.all()
	dcars = {}
	for car in cars:
		brand = str(car.nucleo)
		if brand in dcars:
			dcars[brand].append(car.bairro)
		else:
			dcars[brand] = [car.bairro]
	cars = json.dumps(dcars)
	brands = json.dumps([str(b) for b in brands])
	return render(request, 'geomaraba/regcar.html', {'brands': brands, 'cars': cars, 'opc': 'None'})
	

def testemapa(request):
	brands = Nucleo.objects.all()
	cars = Bairro.objects.all()
	dcars = {}
	for car in cars:
		brand = str(car.nucleo)
		if brand in dcars:
			dcars[brand].append(car.bairro)
		else:
			dcars[brand] = [car.bairro]
	cars = json.dumps(dcars)
	brands = json.dumps([str(b) for b in brands])
	return render(request, 'geomaraba/regcar.html', {'brands': brands, 'cars': cars, 'opc': 'None'})
	
def post(request):	
	if request.method == "POST":
		a = request.POST['drop1']
		#return render(request, 'geomaraba/principal2.html', locals())
		return HttpResponseRedirect('/carro/')