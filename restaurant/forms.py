from django import forms
from .models import Ingredient,Purchase,MenuItem,RecipeRequirement


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = "__all__"

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = "__all__"

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = "__all__"

class RecipeRequirementsForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirement
        fields = "__all__"