from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Tipo)
admin.site.register(Grupo)

class ArchivoAdmin(admin.ModelAdmin):
    list_display=['fecha','tipo','grupo','image','observaciones']
    search_fields=["image"]
    list_filter=['fecha','tipo__nombre','grupo__nombre']



admin.site.register(Archivos, ArchivoAdmin)

