from django.contrib import admin
from Petstagram.photos.models import Photo


# Register your models here.
@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['location', 'description']