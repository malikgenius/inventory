from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Type, Item, VendorType, UserProfile

# Register your models here.
# admin.site.register(Item)
# vendor selection in admin panel..
@admin.register(VendorType)
class VendorTypeAdmin(admin.ModelAdmin):
    list_display = ('vendor_name',)
    search_fields = ('vendor_name',)
    ordering = ['vendor_name', ]

# vendor selection in admin panel..
@admin.register(Type)
class VendorTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ['name', ]


# Custom User Model will need fields to be set so we can add users from admin panel and we can view them as well..
# below code is found on internet from a blog post .. awesome one..
# https://testdriven.io/blog/django-custom-user-model/
@admin.register(UserProfile)
class CustomUserAdmin(UserAdmin):
    list_display = ('name', 'email', 'no_of_items', 'is_staff', 'is_active')
    list_filter = ('name', 'email', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('name', 'email', 'password')}),
        ('Permissions', {
         'fields': ('is_staff', 'is_active', 'is_superuser')})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'email', 'password1', 'password2', 'is_staff', 'is_active', 'is_superuser')}
         ),
    )

    search_fields = ('email', 'name')
    ordering = ('email', 'name', 'is_staff', 'is_active')


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'Type', 'item_model',
                    'purchased_date', 'condition', 'user', 'is_assigned', 'description')
    list_editable = ('is_assigned', 'condition')
    search_fields = ('item_model', 'condition')
    list_filter = ('condition', 'purchased_date')
    autocomplete_fields = ['vendor', 'Type', 'user']
