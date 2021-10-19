import uuid
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    admin = models.BooleanField(default=False)
    date_of_birth = models.DateField(null=True, blank=True)


class ProfileAddress(models.Model):
    id = models.AutoField(primary_key=True)
    street_name = models.CharField(max_length=100)
    level = models.SmallIntegerField()
    unit = models.SmallIntegerField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


# class Users(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     dob = models.DateField(max_length=8)
#     email = models.EmailField(max_length=50)
#     password = models.CharField(max_length=50)
#     admin = models.BooleanField(default=False)
#
#
# class UsersAddresses(models.Model):
#     id = models.AutoField(primary_key=True)
#     street_name = models.CharField(max_length=100)
#     level = models.SmallIntegerField()
#     unit = models.SmallIntegerField()
#     user = models.ForeignKey(Users, on_delete=models.DO_NOTHING, null=True)

