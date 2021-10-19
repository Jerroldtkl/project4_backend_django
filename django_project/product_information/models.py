from django.db import models


# Create your models here.
class Succulents(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='plants')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=50)



