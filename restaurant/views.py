from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import IngredientForm,MenuItemForm,PurchaseForm,RecipeRequirementsForm
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Ingredient,MenuItem,RecipeRequirement,Purchase
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.contrib.auth import logout
# Create your views here.
def home(request):
    return render(request,'restaurant/home.html',{})

class NewIngredientsView(CreateView):
    model = Ingredient
    template_name = "restaurant/add_ingredient.html"
    form_class = IngredientForm

class IngredientView(ListView):
    model=Ingredient
    template_name="restaurant/ingredient_list.html"

class UpdateIngredientView(UpdateView):
    model = Ingredient
    template_name = 'restaurant/update_ingredient.html'
    form_class = IngredientForm
    
class NewMenuItemView(CreateView):
    model=MenuItem
    template_name="restaurant/add_menu_item.html"
    form_class=MenuItemForm

class MenuView(ListView):
    model = MenuItem
    template_name = "restaurant/menu_list.html"

class  NewRecipeRequirementView(CreateView):
    model=RecipeRequirement
    template_name = "restaurant/add_recipe_requirement.html"
    form_class=RecipeRequirementsForm

class NewPurchaseView(CreateView):
    model=Purchase
    template_name="restaurant/add_purchase.html"
    form_class=PurchaseForm

class PurchaseListView(ListView):
    model=Purchase
    template_name="restaurant/purchase_list.html"

class ReportsView(ListView):
    model=Purchase
    template_name = "restaurant/reports.html"


def log_out(request):
    logout(request)
    return redirect ('/')