from django.db import models
from django.contrib.auth.models import User
from products.models import Item


class Location(models.Model):
    name = models.CharField(max_length=100, unique=True)
    budget = models.FloatField(default=10.0)
    manager = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=1)

    def __str__(self): return self.name

class ItemLocation(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='location_items')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='location_items')
    qty = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.item.name}: {self.qty}'