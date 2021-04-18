from django.db import models

class Guitar(models.Model):
	model = models.CharField(max_length=150)
	brand = models.CharField(max_length=100)
	manufacturer = models.CharField(max_length=150)
	description = models.TextField(blank=True, null=True)
	weight =  models.FloatField(blank=True, null=True)

	def __str__(self):
		return '{}, {}'.format(self.model, self.brand)

	class Meta:
		verbose_name_plural = 'Guitars'

class Pedal(models.Model):
	model = models.CharField(max_length=150)
	brand = models.CharField(max_length=100)
	manufacturer = models.CharField(max_length=150)
	description = models.TextField(blank=True, null=True)
	weight =  models.FloatField(blank=True, null=True)

	def __str__(self):
		return f'{str(self.model)}, {str(self.brand)}'

	class Meta:
		verbose_name_plural = 'Pedals'

