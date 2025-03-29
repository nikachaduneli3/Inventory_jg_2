from django.db import models
from core.models import BaseModel
import random


class Category(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

def generate_barcode():
    digits = '0123456789'
    barcode = ''.join([random.choice(digits) for _ in range(13)])
    while Item.objects.filter(barcode=barcode).exists():
        barcode = ''.join([random.choice(digits) for _ in range(13)])
    return barcode



class Item(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    height = models.FloatField(null=True, blank=True)
    width = models.FloatField(null=True, blank=True)
    length = models.FloatField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')
    stock_qty = models.PositiveIntegerField(default=0)
    expiration_date = models.DateField(null=True, blank=True)
    barcode = models.CharField(max_length=13, unique=True,
                               editable=False, default=generate_barcode)



    def __str__(self):
        return self.name
