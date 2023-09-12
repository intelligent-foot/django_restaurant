from django.db import models


# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=200,unique=True)
    price_per_unit = models.FloatField(default=0)
    quantity = models.FloatField(default=0)
    unit = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural =  "Ingredients"
        verbose_name = "Ingredient"
    def __str__(self) :
        return f"""
        name = {self.ingredient_name};
        qty = {self.ingredient_quantity};
        unit = {self.ingredient_unit};
        unit_price = {self.ingredient_price_per_unit}
        """
    
    def get_absolute_path(self):
        return "/ingredients"
    


class MenuItem(models.Model):
    price = models.FloatField(default=0.00)
    title = models.CharField(unique=True, max_length=200)

    class Meta:
        verbose_name_plural = "Menu Items"
        verbose_name = "Menu Item"

    def __str__(self) :
        return f" title = {self.title}; price = {self.price}"
      
    def available(self):
        return all(X.enough() for X in self.reciperequirement_set.all())
        
     
    def get_absolute_path(self):
        return "/menu"

        
class RecipeRequirement(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0)

    class Meta:
        verbose_name_plural = "Recipe Requirements"
        verbose_name = "Recipe Requirement"

    def __str__(self):
        return f"menu_item = [{self.menu_item.__str__()}]; ingredient = {self.ingredient.name}; quantity ={self.quantity}"
    
     
    def get_absolute_path(self):
        return "/menu"
    
    def enough(self):
        return self.quantity <= self.ingredient.quantity

class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural= "Purchases"
        verbose_name = "Purchase"

    def __str__(self):
        return f"menu_items = [{self.menu_item.__str__()}]; time = {self.timestamp}"
    
     
    def get_absolute_path(self):
        return "/purchases"
      

    
        