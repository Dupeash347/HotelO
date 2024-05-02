# models.py

from django.db import models
from django.db.models import Sum
from django.utils import timezone

class MenuCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name


class Order(models.Model):
    table_number = models.CharField(max_length=10)
    items = models.ManyToManyField(MenuItem, related_name='orders')
    status = models.CharField(max_length=10, choices=[('Open', 'Open'), ('Closed', 'Closed')], default='Open')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - Table {self.table_number}"

    def total_price(self):
        return self.items.aggregate(total_price=Sum('price'))['total_price'] or 0