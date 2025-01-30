from django.db import models # type: ignore

# Create your models here.

class Product(models.Model):
    product = models.CharField('product', max_length=200)
    price = models.DecimalField('price', default=0.00, max_digits=9, decimal_places=2)
    created_at = models.DateTimeField('created_at', auto_now_add=True)
    updated_at = models.DateTimeField('updated_at', auto_now=True)
    
    class Meta:
        ordering = ['id']
