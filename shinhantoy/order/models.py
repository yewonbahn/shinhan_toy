from django.db import models
# Create your models here.

class Order(models.Model):
    
    
    class Meta:
        db_table ="shinhan_order"
        verbose_name="주문정보"
        verbose_name_plural ="주문정보"
