from django.db import models
from decimal import Decimal

# Create your models here.
class FoodData(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    protiens = models.DecimalField(max_digits=6, decimal_places=2)
    fat = models.DecimalField(max_digits=6, decimal_places=2)
    calories = models.DecimalField(max_digits=6, decimal_places=2)
    carbohydrates = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='userimg/',blank=True,null=True)

    def __str__(self):
        return self.name


class TrackerData(models.Model):
    name = models.ForeignKey(FoodData, on_delete=models.CASCADE)  # Ensure the model name is correct
    quantity = models.FloatField()
    calories = models.FloatField(default=0)
    proteins = models.FloatField(default=0)
    fat = models.FloatField(default=0)
    carbohydrates = models.FloatField(default=0)

    def save(self, *args, **kwargs):
        food = self.name  # Fetch the selected food item
    
        quantity_decimal = Decimal(str(self.quantity))  # Convert float to Decimal

        self.calories = food.calories * quantity_decimal
        self.proteins = food.protiens * quantity_decimal
        self.fat = food.fat * quantity_decimal
        self.carbohydrates = food.carbohydrates * quantity_decimal

        super().save(*args, **kwargs)  # Save to database