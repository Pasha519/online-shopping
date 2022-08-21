from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django_countries.fields import CountryField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    class Meta:
        ordering = ('name',)
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("category", args=[self.id])
    
        
class Product(models.Model):
    category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    image = models.ImageField(upload_to='products/',blank=True)
    description = models.TextField(blank=True)
    price = models.IntegerField(null=True,blank=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name
    

    def get_absolute_url(self):
        return reverse("product_details", args=[self.id])
    


class Cart(models.Model):
    SIZE_STATUS = (('s', 'S'),
                   ('m', 'M'),
                   ('l', 'L'),
                   ('xl', 'XL'))
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    size = models.CharField(max_length=5, choices=SIZE_STATUS, default='s')
    total = models.PositiveIntegerField(blank=True,null=True)
    def __str__(self):
        return self.product.name
    

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    image = models.ImageField(upload_to="products/", blank=True)
    mobile = models.PositiveIntegerField(null=True,blank=True)
    address = models.CharField(max_length=250,blank=True)
    postal_code = models.CharField(max_length=20,blank=True)
    city = models.CharField(max_length=100,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    country = CountryField(null=True,blank=True)

    class Meta:
        ordering = ('-created',)
    
    def __str__(self):
        return f'Order {self.id}'
    

    


class OrderItem(models.Model):
    PAYMENT = (('gpay', 'Gpay'),
               ('phone pay', 'Phone Pay'),
               ('cash on delivery', 'Cash on delivaey'))
    SIZE_STATUS = (('s', 'S'),
                   ('m', 'M'),
                   ('l', 'L'),
                   ('xl', 'XL'))
    STATUS = (
        ('Pending', 'Pending'),
        ('Order Confirmed', 'Order Confirmed'),
        ('Out for Delivery', 'Out for Delivery'),
        ('Delivered', 'Delivered'),)
    order = models.ForeignKey(Order,related_name='Order',on_delete=models.CASCADE,null=True,blank=True)
    product = models.ForeignKey(Product,related_name='order_items',on_delete=models.CASCADE)
    price = models.IntegerField(null=True,blank=True)
    quantity = models.PositiveIntegerField(default=1)
    total = models.IntegerField(blank=True,null=True)
    size = models.CharField(max_length=5, choices=SIZE_STATUS, default='s')
    payment = models.CharField(max_length=50, choices=PAYMENT, default='cash on delivery')
    status = models.CharField(max_length=50,choices=STATUS,default='Pending')
    
    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity

    class Meta:
        ordering = ("-id",)
