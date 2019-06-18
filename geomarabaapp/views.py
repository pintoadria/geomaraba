from django.shortcuts import render

def principal(request):
    return render(request, 'geomaraba/principal.html', {})
