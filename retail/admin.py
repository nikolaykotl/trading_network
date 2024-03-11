from django.contrib import admin
from django.utils.html import format_html
from rest_framework.reverse import reverse

from retail.models import Contacts, Products, Supplier, Buyer, Trading_network, Debt, Link_trading_network


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'country', 'city', 'street', 'house_number',)
    list_filter = ('email', 'country',)
    search_fields = ('country',)

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'date_of_market_launch',)
    list_filter = ('name',)
    search_fields = ('name',)

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact',)
    list_filter = ('name', 'contact__city')
    search_fields = ('name',)
    filter_horizontal = ['products']


@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    model = Buyer
    list_display = ('id', 'name', 'contact', 'get_name_supplier', 'product')
    list_filter = ('name',)
    search_fields = ('name',)

    def get_name_supplier(self, obj):
        return obj.supplier.name
    get_name_supplier.admin_order_field = 'поставщик'
    get_name_supplier.short_description = 'название поставщика'

@admin.register(Trading_network)
class Trading_networkAdmin(admin.ModelAdmin):
    list_display = ('level_0', 'level_1', 'level_2')
    list_filter = ('level_0',)
    search_fields = ('level_0',)

@admin.register(Link_trading_network)
class Link_trading_networkAdmin(admin.ModelAdmin):
    list_display = ('company', 'supplier', 'contacts', 'products', 'debt', 'creation_time', 'supplier_link')
    list_filter = ('company', 'contacts__city',)
    search_fields = ('company', 'supplier',)

    def supplier_link(self, obj):
        supplier_id = str(Supplier.objects.get(name=obj.supplier).id)
        if obj.supplier:
            return format_html('<a href="%s">%s</a>' % (reverse('retail:supplier_detail', args=supplier_id), "перейти на страницу просмотра Поставщика"))
        else:
            return obj.supplier

@admin.register(Debt)
class DebtAdmin(admin.ModelAdmin):
    list_display = ('buyer', 'supplier', 'debt')
    list_filter = ('buyer', 'supplier')
    search_fields = ('buyer',)
    actions = ['cleaned']

    @admin.action(description="Очистить задолженность перед поставщиком")
    def cleaned(self, request, queryset):
        for qs in queryset:
            print(qs.debt)
            qs.debt=0.00
            qs.save()

