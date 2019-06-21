from django.shortcuts import render
from .models import Dados, Brand, Car
import json

def principal(request):
    return render(request, 'geomaraba/principal.html', {})

def mapa(request):
    mapas = Dados.objects.all() 
    return render(request, 'geomaraba/mapa.html', {'mapas': mapas})
	
	
#def regcar(request):
#	brands = Brand.objects.all()
	#cars = Car.objects.all()
	#dcars = {}
	#for car in cars:
	#	brand = str(car.brand)
	#	if brand in dcars:
	#		dcars[brand].append(car.name)
	#	else:
	#		dcars[brand] = [car.name]
	#cars = json.dumps(dcars)
	#brands = json.dumps([str(b) for b in brands])
#	return render(request, 'core/regcar.html', {'brands': brands, 'cars': cars, 'opc': 'None'})