from django.contrib import admin

# Register your models here.
from Petstagram.pets.models import Pet


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'date_of_birth']
