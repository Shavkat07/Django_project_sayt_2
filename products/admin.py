from django.contrib import admin
from products.models import ProductCategory, Product, Basket


# admin.site.register(ProductCategory)
@admin.register(ProductCategory)
class ProductsCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    fields = ('name', 'description')
    readonly_fields = ('description',)
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('image', 'name', 'description', ('price', 'quantity'), 'category')
    readonly_fields = ('description',)
    search_fields = ('name',)
    ordering = ('name',)


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
    extra = 0
