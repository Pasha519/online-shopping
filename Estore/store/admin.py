from django.contrib import admin
from django.contrib.auth.models import User
from store.models import Category,Product,Cart,Order,OrderItem


# Register your models here.
class ProductAdmin(admin.TabularInline):
    model = Product
    prepopulated_fields = {'slug':('name',)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        ProductAdmin
    ]
    list_display = ["id","name","slug"]
    list_display_links = ["id","name","slug"]
    prepopulated_fields = {'slug':('name',)}

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ["customer","product","quantity"]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "customer", "address",
                    "city", "postal_code", "paid", "created"]
    list_display_links = ["id","customer"]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ["id","order","product","price","quantity","total","size",'payment','status']
    list_display_links = ["id","order","product"]