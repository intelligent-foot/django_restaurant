from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('ingredients/',views.IngredientView.as_view(),name="ingredients"),
    path('menu/', views.MenuView.as_view(),name='menu'),
    path('menu/new',views.NewMenuItemView.as_view(), name='add_menu_item'),
    path('ingredient/new',views.NewIngredientsView.as_view(),name='add_ingredient'),
    path('ingredient/<slug:pk>/update',views.UpdateIngredientView.as_view(),name='update_ingredient'),
    path('reports',views.ReportsView.as_view(),name='reports'),
    path('purchases/',views.PurchaseListView.as_view(),name='purchases'),
    path('purchases/new',views.NewPurchaseView.as_view(),name='add_purchase'),
    path('reciperequirement/new',views.NewRecipeRequirementView.as_view(),name='add_recipe_requirement'),
    path('logout/', views.log_out, name='logout'),
 
    path('accounts/login/',auth_views.LoginView.as_view(),name='login')



]