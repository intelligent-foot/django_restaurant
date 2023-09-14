from django.shortcuts import redirect
from django.core.exceptions import SuspiciousOperation
from .forms import IngredientForm,MenuItemForm,RecipeRequirementsForm
from django.views.generic.edit import CreateView,UpdateView
from .models import Ingredient,MenuItem,RecipeRequirement,Purchase
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView,TemplateView
from django.contrib.auth import logout
from django.db.models import Sum,F

# Create your views here.


class HomeView(LoginRequiredMixin,TemplateView):
    template_name='restaurant/home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ingredients'] = Ingredient.objects.all()
        context['menu_items'] = MenuItem.objects.all()
        context['purchases'] =Purchase.objects.all()
        return context
    



class NewIngredientsView(LoginRequiredMixin,CreateView):
    model = Ingredient
    template_name = "restaurant/add_ingredient.html"
    form_class = IngredientForm




class IngredientView(LoginRequiredMixin,ListView):
    model=Ingredient
    template_name="restaurant/ingredient_list.html"




class UpdateIngredientView(LoginRequiredMixin,UpdateView):
    model = Ingredient
    template_name = 'restaurant/update_ingredient.html'
    form_class = IngredientForm



    
class NewMenuItemView(LoginRequiredMixin,CreateView):
    model=MenuItem
    template_name="restaurant/add_menu_item.html"
    form_class=MenuItemForm




class MenuView(LoginRequiredMixin,ListView):
    model = MenuItem
    template_name = "restaurant/menu_list.html"




class  NewRecipeRequirementView(LoginRequiredMixin,CreateView):
    model=RecipeRequirement
    template_name = "restaurant/add_recipe_requirement.html"
    form_class=RecipeRequirementsForm




class NewPurchaseView(LoginRequiredMixin,TemplateView):
    template_name="restaurant/add_purchase.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu_items"] = [X for X in MenuItem.objects.all() if X.available()]
        return context
    
    def post(self,request):
        menu_item_id =request.POST["menu_item"]
        menu_item = MenuItem.objects.get(pk=menu_item_id)
        requirements = menu_item.reciperequirement_set
        purchase = Purchase(menu_item=menu_item)

        for requirement in requirements.all():
            required_ingredient = requirement.ingredient
            required_ingredient.quantity -= requirement.quantity
            required_ingredient.save()
        purchase.save()
        return redirect('/purchases')
    

   

class PurchaseListView(LoginRequiredMixin,ListView):
    model=Purchase
    template_name="restaurant/purchase_list.html"




class ReportsView(LoginRequiredMixin,TemplateView):
  
    template_name = "restaurant/reports.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["purchases"]=Purchase.objects.all()
        revenue=Purchase.objects.aggregate(
            revenue = Sum("menu_item__price"))["revenue"]
    
        total_cost = 0
        for purchase in Purchase.objects.all():
            for recipe_requirement in purchase.menu_item.reciperequirement_set.all():
                total_cost += recipe_requirement.ingredient.price_per_unit * \
                    recipe_requirement.quantity
        context["revenue"]=revenue
        context["total_cost"]=total_cost
        

        return context
    



def log_out(request):
    logout(request)
    return redirect ('/')




