# from django.db import models
# from django.contrib.auth.models import User
# from product_information.models import Succulents

# Create your models here.


# class Statuses(models.Model):
#     status = models.CharField(primary_key=True, max_length=10)
#
#
# class Usercarts(models.Model):
#     id = models.AutoField(primary_key=True)
#     quantity = models.IntegerField(default=0)
#     total_price = models.SmallIntegerField()
#     user_id = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING)
#     product_id = models.ForeignKey(Succulents, on_delete=models.DO_NOTHING)
#     status = models.ForeignKey(Statuses, on_delete=models.DO_NOTHING)
#
#
# class Usercarts2(models.Model):
#     id = models.AutoField(primary_key=True)
#     quantity = models.IntegerField(default=0)
#     total_price = models.SmallIntegerField()
#     user_id = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING)
#     product_id = models.ForeignKey(Succulents, on_delete=models.DO_NOTHING)
#     status = models.ForeignKey(Statuses, on_delete=models.DO_NOTHING)


