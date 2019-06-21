from django.urls import path
from . import views

urlpatterns = [
	path('', views.principal, name='principal'),
	path('mapa/', views.mapa, name='mapa'),	
	path(r'^regcar/$', views.regcar, name='regcar'),
]