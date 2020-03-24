from django.contrib import admin
from .models import Pet, Feeding, Playground

admin.site.register(Pet)
admin.site.register(Feeding)
admin.site.register(Playground)