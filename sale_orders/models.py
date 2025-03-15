from django.db import models
from core.models import BaseModel
from products.models import Item

NAME_LENGTH = 7

def generate_name():
    prefix = 'S'+'0'*(NAME_LENGTH-1)
    last_purchase =  SaleOrder.objects.order_by('-id').first()
    if not last_purchase: return 'S000001'
    id_length = len(str(last_purchase.id))
    return  f'{prefix[:NAME_LENGTH-id_length]}{last_purchase.id+1}'

class SaleOrder(BaseModel):
    name = models.CharField(max_length=NAME_LENGTH, default=generate_name, editable=False, unique=True)
    completed = models.BooleanField(default=False, editable=False)

    def __str__(self):return self.name

class SaleOrderItem(BaseModel):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="sale_items")
    qty = models.PositiveIntegerField(default=0)
    sale_order = models.ForeignKey(SaleOrder, on_delete=models.CASCADE, related_name='sale_items')
