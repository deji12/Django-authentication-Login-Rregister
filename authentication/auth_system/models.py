from django.db import models
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType


def create_groups():
    # Create the 'Staff' group
    staff_group, created = Group.objects.get_or_create(name="Staff")

    # Create the 'Customer' group
    customer_group, created = Group.objects.get_or_create(name="Customer")


class StaffProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    # Add more fields as needed


class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    building_number = models.IntegerField()
    street = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    apartment_number = models.IntegerField()
    state = models.CharField(max_length=128)
    zipcode = models.IntegerField()
    passport_number = models.CharField(max_length=128)
    passport_expiration = models.DateField()
    passport_country = models.CharField(max_length=128)
    date_of_birth = models.DateField()
