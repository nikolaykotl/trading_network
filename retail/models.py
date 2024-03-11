from datetime import datetime

import psycopg2
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from users.models import NULLABLE


class Contacts(models.Model):
    email = models.EmailField(verbose_name='электронная почта')
    country = models.CharField(max_length=50, verbose_name='страна')
    city = models.CharField(max_length=75, verbose_name='город')
    street = models.CharField(max_length=75, verbose_name='улица')
    house_number = models.CharField(max_length=5, verbose_name='номер дома')

    def __str__(self):
        return f'{self.email}, {self.country}, {self.city}, {self.street}, {self.house_number}'

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'

class Products(models.Model):
    name = models.CharField(max_length=120, verbose_name='название')
    model = models.CharField(max_length=120, verbose_name='модель')
    date_of_market_launch = models.DateField(verbose_name='дата выхода на рынок')

    def __str__(self):
        return f'{self.name}: модель {self.model}, дата выхода на рынок {self.date_of_market_launch}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

class Supplier(models.Model):

    name = models.CharField(max_length=120, verbose_name='название')
    contact = models.ForeignKey(Contacts, on_delete=models.CASCADE, verbose_name='контакт')
    products = models.ManyToManyField(Products, verbose_name='продукты')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'поставщик'
        verbose_name_plural = 'поставщики'

class Buyer(models.Model):
    name = models.CharField(max_length=120, verbose_name='название')
    contact = models.ForeignKey(Contacts, on_delete=models.CASCADE, verbose_name='контакт')
    product = models.CharField(max_length=250, verbose_name='продукты', **NULLABLE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name='поставщик')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'покупатель'
        verbose_name_plural = 'покупатели'

@receiver(pre_save, sender=Buyer)
def create_product_buyer(sender, instance, **kwargs):
    buyer = instance
    suppliers = Supplier.objects.all()
    products = Products.objects.all()
    product_list = []
    products_buyer = ''
    for supplier in suppliers:
        if buyer.supplier_id == supplier.id:
            conn = psycopg2.connect(database='retail', user='postgres', password='9501718367', host='127.0.0.1')
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM retail_supplier_products')
            for product in cursor.fetchall():
                if product[1] == buyer.supplier_id:
                    prod = Products.objects.get(id=product[2])
                    product_list.append(prod)
            products_buyer = ', '.join(str(element) for element in product_list)
            cursor.close()
            conn.close()
    buyer.product = products_buyer

class Trading_network(models.Model):
    level_0 = models.CharField(max_length=120, verbose_name='компания - Уровень_0')
    level_1 = models.CharField(max_length=120, verbose_name='компания - Уровень_1', **NULLABLE)
    level_2 = models.CharField(max_length=120, verbose_name='компания - Уровень_2', **NULLABLE)



    def __str__(self):
        return f'Уровень_0 - {self.level_0}: Уровень_1 - {self.level_1}, Уровень_2 - {self.level_2}'

    class Meta:
        verbose_name = 'торговая сеть'
        verbose_name_plural = 'торговая сеть'

@receiver(post_save, sender=Buyer)
@receiver(post_save, sender=Supplier)
def create_trading_network(sender, instance, **kwargs):

    if Buyer.objects.filter(name=instance).exists() and Supplier.objects.filter(name=instance).exists(): #если компания покупающая товар у поставщика существует
        supplier_id = Buyer.objects.get(name=instance).supplier_id # id поставщика
        name_sup = Supplier.objects.get(id=supplier_id).name
        sup_id = Supplier.objects.get(name=instance).id
        if Buyer.objects.filter(supplier_id=sup_id).exists():
            buyers = Buyer.objects.filter(supplier_id=sup_id)
            for buyer in buyers:
                buyer_name = buyer.name
                Trading_network.objects.get_or_create(level_0=name_sup, level_1=instance, level_2=buyer_name)
        else:
            Trading_network.objects.get_or_create(level_0=supplier_id, level_1=instance, level_2='')
    elif Buyer.objects.filter(name=instance).exists() == True and Supplier.objects.filter(name=instance).exists() == False:
        sup_lev_m1_id = Buyer.objects.get(name=instance).supplier_id  # id поставщика уровня минус 1 к уровню покупателя
        name_sup_lev_m1 = Supplier.objects.get(id=sup_lev_m1_id).name # название поставщика уровня минус 1 к уровню покупателя
        if Buyer.objects.filter(name=name_sup_lev_m1).exists(): #проверка существования поставщика уровня минус 2 уровня к уровню покупателя
            sup_lev_m2_id = Buyer.objects.get(name=name_sup_lev_m1).supplier_id  # id поставщика уровня минус 2 к уровню покупателя
            name_sup_lev_m2 = Supplier.objects.get(id=sup_lev_m2_id).name # название поставщика уровня минус 2 к уровню покупателя
            Trading_network.objects.get_or_create(level_0=name_sup_lev_m2, level_1=name_sup_lev_m1,
                                                     level_2=instance)
        else:
            Trading_network.objects.get_or_create(level_0=name_sup_lev_m1, level_1=instance, level_2='')

    elif Buyer.objects.filter(name=instance).exists() == False and Supplier.objects.filter(name=instance).exists() == True:
        if Buyer.objects.filter(supplier_id=instance.id).exists() == False:
            Trading_network.objects.get_or_create(level_0=instance, level_1='', level_2='')
        else:
            name_buyer_p1 = Buyer.objects.get(supplier_id=instance.id).name
            is_buyer_p2 = Buyer.objects.filter(name=name_buyer_p1).exists()
            if is_buyer_p2 == False:
                supplier_id = Supplier.objects.get(name=name_buyer_p1).id
                name_buyer_p2 = Supplier.objects.get(supplier_id=supplier_id).name
                Trading_network.objects.get_or_create(level_0=instance, level_1=name_buyer_p1,
                                                         level_2=name_buyer_p2)
            else:
                Trading_network.objects.get_or_create(level_0=instance, level_1=name_buyer_p1,
                                                             level_2='')

class Debt(models.Model):
    buyer = models.CharField(max_length=120, verbose_name='покупатель')
    supplier = models.CharField(max_length=120, verbose_name='поставщик')
    debt = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='задолженность', **NULLABLE)

    def __str__(self):
        return self.buyer

    class Meta:
        verbose_name = 'задолженность перед поставщиком'
        verbose_name_plural = 'задолженность перед поставщиком'

@receiver(post_save, sender=Buyer)
def create_debt_supplier(sender, instance, **kwargs):
    buyer = instance.name
    supplier_id = Buyer.objects.get(name=buyer).supplier_id
    supplier = Supplier.objects.get(id=supplier_id)
    Debt.objects.get_or_create(buyer=buyer, supplier=supplier)

class Link_trading_network(models.Model):

    company = models.CharField(max_length=120, verbose_name='компания')
    supplier = models.CharField(max_length=120, verbose_name='поставщик', **NULLABLE)
    contacts = models.ForeignKey(Contacts, on_delete=models.CASCADE, verbose_name='контакт')
    products = models.CharField(max_length=250, verbose_name='продукты', **NULLABLE)
    debt = models.DecimalField(max_digits=12, decimal_places=2,  verbose_name='задолженность', **NULLABLE)
    creation_time = models.DateTimeField(auto_created=True, verbose_name='время создания', **NULLABLE)

    def __str__(self):
        return f'{self.company}: задолженность {self.debt}, контакты {self.contacts}'

    class Meta:
        verbose_name = 'звено торговой сети'
        verbose_name_plural = 'звенья торговой сети'

@receiver(post_save, sender=Buyer)
def create_link_trading_network(sender, instance, **kwargs):
    print(instance)
    if sender == Buyer:
        if Link_trading_network.objects.filter(company=instance).exists() == False:
            id = Buyer.objects.get(name=instance).supplier_id
            supplier = Supplier.objects.get(id=id)
            contacts_id = Buyer.objects.get(name=instance).contact_id
            contact = Contacts.objects.get(id=contacts_id)
            print(contact.city)
            products = Buyer.objects.get(name=instance).product
            debt = Debt.objects.get(buyer=instance).debt
            creation_time = datetime.now()
            Link_trading_network.objects.get_or_create(company=instance, supplier=supplier, contacts=contact, products=products, debt=debt, creation_time=creation_time)

@receiver(pre_save, sender=Debt)
def create_link_trading_network(sender, instance, **kwargs):
    if Link_trading_network.objects.filter(company=instance).exists():
        link = Link_trading_network.objects.get(company=instance)
        link.debt = instance.debt
        link.save()
