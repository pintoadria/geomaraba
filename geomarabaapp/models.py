from django.db import models
from django.utils import timezone
import json

class Nucleo(models.Model):
	nucleo = models.CharField(max_length=200)
	descricao = models.TextField()
	
	def __str__(self):
		return u'Núcleo/Zona/Distrito: %s' % (self.nucleo)

class Bairro(models.Model):
	nucleo = models.ForeignKey(Nucleo, on_delete=models.PROTECT)
	bairro = models.CharField(max_length=200)
	descricao = models.TextField()
	kml = models.FileField(upload_to='uploads/')
	dwg = models.FileField(upload_to='uploads/')
	pdf = models.FileField(upload_to='uploads/')

	def __str__(self):
		return u'Núcleo/Zona/Distrito: %s - Bairro: %s' % (self.nucleo.nucleo, self.bairro)
		
class Quadra(models.Model):
	bairro = models.ForeignKey(Bairro, on_delete=models.PROTECT)
	quadra = models.CharField(max_length=200)
	descricao = models.TextField()
	kml = models.FileField(upload_to='uploads/')
	dwg = models.FileField(upload_to='uploads/')
	pdf = models.FileField(upload_to='uploads/')

	def __str__(self):
		return u'Bairro: %s - Quadra: %s' % (self.bairro.bairro, self.quadra)
	
class Dados(models.Model):
	regiao = models.CharField(max_length=200)
	bairro = models.CharField(max_length=200)
	descricao = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	kml = models.FileField(upload_to='uploads/')
	dwg = models.FileField(upload_to='uploads/')
	pdf = models.FileField(upload_to='uploads/')
	
	#published_date = models.DateTimeField(
	#	blank=True, null=True)

	#def publish(self):
	#	self.published_date = timezone.now()
	#	self.save()

	def __str__(self):
		return u'%s %s' % (self.regiao, self.bairro)
		
		
class Brand(models.Model):
	company_name = models.CharField(max_length=100)
	teste = models.CharField(max_length=200)
	
	def __str__(self):
		return u'%s %s' % (self.company_name, self.teste)
	
class Car(models.Model):
	brand = models.ForeignKey(Brand, on_delete=models.PROTECT)
	name = models.CharField(max_length=100)

	def __str__(self):
		return u'Name: %s Marca:%s' % (self.name, self.brand.company_name)
		#return {'name': self.name, 'brand': self.brand.company_name}
#		return u'%s %s' % (self.regiao, self.bairro)