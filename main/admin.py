from django.contrib import admin
from .models import Reservoirs, TextFile, ChemistryData

# Register your models here.
admin.site.register(Reservoirs)
admin.site.register(TextFile)
admin.site.register(ChemistryData)