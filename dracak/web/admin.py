from django.contrib import admin
from .models import Place, Option, Character

# Register your models here.


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
	pass


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
	pass


@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
	pass

