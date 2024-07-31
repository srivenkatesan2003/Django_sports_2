from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    product_id=models.IntegerField()
    price = models.IntegerField()


    def __str__(self) -> str:
        return self.name
    