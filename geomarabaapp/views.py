from django.shortcuts import render
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
	brands = Brand.objects.all()
	cars = Car.objects.all()
	dcars = {}
	for car in cars:
		brand = str(car.brand)
		if brand in dcars:
			dcars[brand].append(car.name)
		else:
			dcars[brand] = [car.name]
	cars = json.dumps(dcars)
	brands = json.dumps([str(b) for b in brands])
	return render(request, 'geomaraba/regcar.html', {'brands': brands, 'cars': cars, 'opc': 'None'})
	
def testemapa(request):
	nucleo = Nucleo.objects.all()
	bairro = Bairro.objects.all()
	dcars = {}
	for bairro in bairro:
		nucleo = str(bairro.nucleo)
		if nucleo in dcars:
			dcars[nucleo].append(bairro.bairro)
		else:
			dcars[nucleo] = [bairro.bairro]
	bairro = json.dumps(dcars)
	nucleo = json.dumps([str(b) for b in nucleo])
	return render(request, 'geomaraba/testemapa.html', {'nucleo': nucleo, 'bairro': bairro, 'opc': 'None'})	