from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    daily_rental_fee = models.DecimalField(max_digits=2, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    barcode = models.CharField(max_length=255)


class UserTypes(models.Model):
    user_type = models.CharField(max_length=55, null=False)


class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=55, unique=True)
    phone = models.CharField(max_length=55)
    birth_date = models.DateField(null=True)
    is_suspended = models.BooleanField(default=False)
    user_type = models.ForeignKey(
        UserTypes, on_delete=models.DO_NOTHING)


class Coupons(models.Model):
    coupon_name = models.CharField(max_length=255)
    coupon_rate = models.DecimalField(max_digits=2, decimal_places=2)


class Rentals(models.Model):
    rent_date = models.DateTimeField(auto_now=True)
    return_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(Users, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    coupon = models.ForeignKey(Coupons, on_delete=models.DO_NOTHING)
