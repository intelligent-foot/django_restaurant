from django.contrib import admin

# Register your models here.
from .models import Purchase,RecipeRequirement,Ingredient,MenuItem


admin.site.register(Purchase)
admin.site.register(RecipeRequirement)
admin.site.register(MenuItem)
admin.site.register(Ingredient)