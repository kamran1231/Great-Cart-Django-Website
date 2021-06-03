from django.contrib import admin
from .models import Product

# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':['product_name']}
    list_display = ['id','product_name','price','stock','category',
                    'created_date','modified_date','is_available']

