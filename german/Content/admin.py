from django.contrib import admin
from .models import Card, Intro, Service, Slider

# Register your models here.
admin.site.register([Card, Intro, Service, Slider])