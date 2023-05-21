import django.contrib.admin

import products.models


@django.contrib.admin.register(products.models.Category)
class CategoryAdmin(django.contrib.admin.ModelAdmin):
    """категория в админке"""

    list_display = ('id', 'name')
    list_display_links = ('id',)


@django.contrib.admin.register(products.models.Product)
class ProductAdmin(django.contrib.admin.ModelAdmin):
    """продукт в админке"""

    list_display = ('id', 'name', 'is_published')
    list_display_links = ('id',)
    list_editable = ('is_published',)
    list_filter = ('is_published',)
