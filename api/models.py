from django.db import models
from django.conf import settings
# from django.contrib.auth.models import User
# User Models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

from rest_framework.response import Response


class UserProfileManager(BaseUserManager):
    ##  Manager for users Profiles###

    def create_user(self, email, name, password):
        ## Create a new user Profile###
        if not email:
            raise ValueError("User must have an email address")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        ### we have to set encrypted password for user ###
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        ## Create and save a new Superuser with given details ###
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    ### Database model for users in the System###
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        ## Retrieve full name of user ###
        return self.name

    def get_short_name(self):
        ## Retrieve short name of user###
        return self.name

    def __str__(self):
        ##return string representation of a user###
        return self.email

    # Custom function in model, can be done in views as well ..awesome we can get all required info from here ..
    def no_of_items(self):
        items = Item.objects.filter(user=self)
        return len(items)

    def item_details(self):

        items = Item.objects.filter(user=self)

        for item in items:

            return item.purchased_date

# Vendor Type Class


class VendorType(models.Model):
    vendor_name = models.CharField(max_length=50)

    def __str__(self):
        return self.vendor_name.lower()


# ITEM TYPE Class
class Type(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name.lower()


# Item Class where all the fields will be added
class Item(models.Model):
    # item_vendor = models.ForeignKey(
    #     VendorType, on_delete=models.CASCADE, related_name='none', null=True)
    vendor = models.ManyToManyField(
        VendorType)
    # models.SET_NULL will set it to null if type was deleted, for example we added laptop to type but we deleted that laptop, with below code our field will be null.
    # models.CASCADE will delete our Item if type was deleted .. means we remove laptop from type all the items who have type laptop will be deleted  .. which is good in this case
    Type = models.ForeignKey(
        'Type', on_delete=models.SET_NULL, default='', null=True, blank=True)
    # Below can be imported from local model UserProfile but best to import it from settings.AUTH this way if we change auth settings in future wont need to change it in all models.
    # user = models.ForeignKey(
    #     'UserProfile', on_delete=models.SET_NULL, default='', null=True, blank=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, default='', null=True, blank=True
    )

    item_model = models.CharField(max_length=50, default='')
    service_tag = models.CharField(
        max_length=50, default='', blank=True, unique=True)
    purchased_date = models.DateField(blank=True, null=True)
    condition = models.CharField(max_length=50, default='')
    is_assigned = models.BooleanField(default=False)
    description = models.TextField(max_length=500, default='', blank=True)

    # def __str__(self):
    #     return self.item_model,

    # change all to lowercase pre-save ...

    def save(self, *args, **kwargs):
        self.condition = self.condition.lower()
        return super(Item, self).save(*args, **kwargs)
