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
	if request.method == "GET" and request.is_ajax():
		bairro = request.GET.get("kml")
		try:
			bairro = Bairro.objects.get(kml = kml)
		except:
			return JsonResponse({"success":False}, status=400)
		user_info = {
			"kml": bairro.kml,
			#"last_name": user.last_name,
			#"email": user.email,
			#"is_active": user.is_active,
			#"joined": user.date_joined
		}
		return JsonResponse({"user_info":user_info}, status=200)
	return JsonResponse({"success":False}, status=400)
	
	
	if request.method == "POST":
		a = request.POST['drop1']
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
		#return render(request, 'geomaraba/regcar.html', locals())
		return HttpResponseRedirect('/carro/')
		#return HttpResponseRedirect(reverse('/carro/'))
		
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
    if request.method == "POST": #os request.GET()
        get_value= request.body
        # Do your logic here coz you got data in `get_value`
        data = {}
        data['result'] = 'you made a request'
        return HttpResponse(json.dumps(data), content_type="application/json")	
		
def teste_ajax(request, id_):
    return HttpResponse('Id recebido via AJAX: <strong>{0}</strong>'.format(id_), mimetype='text/html')


	