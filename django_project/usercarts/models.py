from django.db import models
from user_information.models import Profile
from product_information.models import Succulents

# Create your models here.


class Statuses(models.Model):
    status = models.CharField(primary_key=True, max_length=10)


class Usercarts(models.Model):
    id = models.AutoField(primary_key=True)
    quantity = models.IntegerField(default=0)
    total_price = models.SmallIntegerField()
    user_uuid = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    product_id = models.ForeignKey(Succulents, on_delete=models.DO_NOTHING)
    status = models.ForeignKey(Statuses, on_delete=models.DO_NOTHING)



