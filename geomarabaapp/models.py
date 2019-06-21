from django.db import models
from django.utils import timezone
import json

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
	
#class Car(models.Model):
#	brand = models.ForeignKey(Brand)
#	name = models.CharField(max_length=100)

#	def __str__(self):
#		return {'name': self.name, 'brand': self.brand.company_name}