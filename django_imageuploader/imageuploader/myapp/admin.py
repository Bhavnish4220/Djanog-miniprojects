from django.contrib import admin
from .models import image

@admin.register(image)
class imageadmin(admin.ModelAdmin):
    list_display=['id','photo','date']