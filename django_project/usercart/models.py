from django.db import models
from django.contrib.auth.models import User
from product_information.models import Succulents

# Create your models here.


class Usercart(models.Model):
    id = models.AutoField(primary_key=True)
    quantity = models.IntegerField(default=0)
    total_price = models.SmallIntegerField()
    user = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Succulents, on_delete=models.DO_NOTHING)
    status = models.CharField(default='Close', max_length=10)
