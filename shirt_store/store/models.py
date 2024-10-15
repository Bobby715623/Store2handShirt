from django.db import models
from django.contrib.auth.models import Group

# Create your models here.
class Admin(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=20)
    group = models.ManyToManyField(Group)
class Customer(models.Model):
    username = models.CharField(max_length=255,null=False)
    first_name = models.CharField(max_length=255,null=False)
    last_name = models.CharField(max_length=255,null=False)
    group = models.ManyToManyField(Group)
    phone = models.CharField(max_length=255,null=False)
    email= models.EmailField(null=False)
    password = models.CharField(max_length=255,null=False)
    birthday = models.DateField(null=False)
    last_login = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
class CustomerAdress(models.Model):
    customer_id = models.ForeignKey(Customer,on_delete=models.CASCADE)
    province = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    subdistrict = models.CharField(max_length=255)
    post_num = models.IntegerField()
    addressinfo = models.TextField()
class Coupon(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    discount = models.IntegerField()
    amount = models.IntegerField()
    expire_date = models.DateField()
class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
class Band(models.Model):
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    about = models.TextField()
    category_band = models.ManyToManyField(Category)
class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)
    description = models.TextField()
    band_id=models.ForeignKey(Band, on_delete=models.CASCADE)
class Order(models.Model):
    customer_id = models.ForeignKey(Customer,on_delete=models.CASCADE)
    total_price = models.IntegerField()
    paymentmethod = models.CharField(max_length=255)
    orderstatus = models.CharField(max_length=255)
    create_date  = models.DateTimeField(auto_now = True)
    couponid = models.ForeignKey(Coupon,on_delete=models.CASCADE)
    orderproduct = models.ManyToManyField(Product)    
class Cart(models.Model):
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer,on_delete=models.CASCADE)
    amount = models.IntegerField(null=False)
    price = models.IntegerField(null=False)