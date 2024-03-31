from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.name}"
    

    def get_absolute_url(self):
        return reverse("myshop:product-list-by-category", args=[self.id])
    


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    count = models.PositiveIntegerField()
    image = models.ImageField(default='product-images/default.jpg')

    def __str__(self) -> str:
        return f"{self.name}"
    
    def get_absolute_url(self):
        return reverse("myshop:product-detail", args=[self.id])
    
