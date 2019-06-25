from django.urls import path
from . import views

urlpatterns = [
	path('', views.principal, name='principal'),
	path('mapa/', views.mapa, name='mapa'),	
	path('carro/', views.regcar, name='carro'),
	path('teste/', views.principal2, name='principal2'),
	path('testemapa/', views.testemapa, name='testemapa'),
	#path('teste_ajax/(\d+)/$', views.teste_ajax, name='teste_ajax'),
	
	
	(r'^teste_ajax/(\d+)/$', 'app.views.teste_ajax'),
	
	
	
]