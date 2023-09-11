from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=200,unique=True)
    price_per_unit = models.FloatField(default=0)
    quantity = models.FloatField(default=0)
    unit = models.CharField(max_length=200)

    class Meta:
        verbose_name =  "Ingredients"

    def __str__(self) :
        return f"""
        name = {self.ingredient_name};
        quantity = {self.ingredient_quantity};
        unit = {self.ingredient_unit};
        unit_price = {self.ingredient_price_per_unit}
        """
    
    def get_absolute_path(self):
        return "/ingredients"
    


class MenuItem(models.Model):
    price = models.FloatField(default=0.00)
    title = models.CharField(unique=True, max_length=200)

    class Meta:
        verbose_name = "Menu Item"

    def __str__(self) :
        return f"""
        title = {self.title};
        price = {self.price};
        """
     
    def get_absolute_path(self):
        return "/menu"

        
class RecipeRequirement(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0)

    class Meta:
        verbose_name = "Recipe Requirements"

    def __str__(self):
        return f"menu_item = [{self.menu_item.__str__()}]; ingredient = {self.ingredient.ingredient_name}; quantity ={self.quantity}"
    
     
    def get_absolute_path(self):
        return "/menu"

class Purchase(models.Model):
    purchase_items = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = "Purchases"

    def __str__(self):
        return f"items = [{self.purchase_items.__str__()}]; time = {self.timestamp}"
    
     
    def get_absolute_path(self):
        return "/purchases"
      

    
        