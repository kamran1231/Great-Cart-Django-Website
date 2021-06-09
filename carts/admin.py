from django.contrib import admin
from .models import Cart_item,Cart


# Register your models here.

@admin.register(Cart_item)
class Cart_item_Admin(admin.ModelAdmin):
    list_display = ['id','product','cart','quantity','is_active']

@admin.register(Cart)
class Cart_Admin(admin.ModelAdmin):
    list_display = ['id','cart_id','date_added']