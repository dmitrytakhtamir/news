from .models import *
from django.forms import ModelForm
from django import forms

class NewGuitar(forms.ModelForm):
	class Meta:
		model = Guitar
		fields = '__all__'

class NewPedal(forms.ModelForm):
	class Meta:
		model = Pedal
		fields = '__all__'
