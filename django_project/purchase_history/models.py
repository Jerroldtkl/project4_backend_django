from django.db import models
from user_information.models import Profile
from product_information.models import Succulents
# Create your models here.


class PurchaseHistory(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_quantity = models.IntegerField(default=50)
    purchase_name = models.CharField(max_length=50)
    user_uuid = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    product_id = models.ForeignKey(Succulents, on_delete=models.DO_NOTHING)

