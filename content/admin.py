from django.contrib import admin
from .models import *

models_list = (Guitar, Pedal)

for model in models_list:
	admin.site.register(model)