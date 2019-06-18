from django.shortcuts import render

def principal(request):
    return render(request, 'geomaraba/principal.html', {})

def mapa(request):
    mapas = Dados.objects.all() 
    return render(request, 'geomaraba/mapa.html', {'mapas': mapas})