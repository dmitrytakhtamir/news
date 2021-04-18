from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.http import Http404, HttpResponseRedirect, HttpResponse
from .scraper import *
import requests
from bs4 import BeautifulSoup
import re
import sys

def home(request):
	guitars = Guitar.objects.all()
	pedals = Pedal.objects.all()

	obj = Lenta()
	obj_list = []
	for i in obj:
		obj_list.append(Obj(i[0], i[1]))

	#print(sys.getsizeof(gen), sys.getsizeof(result))

	context = {'guitars': guitars, 'pedals': pedals,
	'obj': obj, 'obj_list': obj_list}

	return render(request, 'home.html', context)

def new_guitar(request):
	form = NewGuitar()
	if request.method == 'POST':
		form = NewGuitar(request.POST)
		if form.is_valid():
			form.save()

			return redirect('home')


	context = {'form': form}
	return render(request, 'new_guitar.html', context)

def new_pedal(request):
	form = NewPedal
	if request.method == 'POST':
		form = NewPedal(request.POST)
		if form.is_valid():
			form.save()

			return redirect('home')

	context = {'form': form}
	return render(request, 'new_pedal.html', context)

def guitar(request, guitar_id):
	guitar = Guitar.objects.get(id=guitar_id)
	output = ('guitar.model', 'guitar.brand')

	context = {'guitar': guitar, 'output': output}
	return render(request, 'guitar.html', context)
