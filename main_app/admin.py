from django.contrib import admin

from .models import Product, Order, OrderItem, Customer


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("product_name", "product_id", "price", "quantity", "status", "created_at")
    search_fields = ("product_name", "product_id", "brand")
    list_filter = ("status", "brand")


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "customer", "order_date", "total_amount", "created_at")
    search_fields = ("id", "customer__registered_name")
    list_filter = ("order_date",)
    inlines = [OrderItemInline]

admin.site.register(Customer)
