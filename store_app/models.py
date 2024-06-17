from django.db import models
from django.utils import timezone
# from ckeditor.fields import RichTextField
from tinymce.models import HTMLField
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Categories"  # This prevents Django from appending 's'

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Color(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Filter_Price(models.Model):
    FILTER_PRICE = (
        ('1 To 1000', '1 To 1000'),
        ('1000 To 5000', '1000 To 5000'),
        ('5000 To 10000', '5000 To 10000'),
        ('10000 To 20000', '10000 To 20000'),
        ('20000 To 30000', '20000 To 30000'),
        ('30000 To 40000', '30000 To 40000'),
        ('40000 To 50000', '40000 To 50000'),
        ('50000 To 60000', '50000 To 60000'),
        ('60000 To 70000', '60000 To 70000'),
        ('70000 To 80000', '70000 To 80000'),
        ('80000 To 90000', '80000 To 90000'),
        ('90000 To 100000', '90000 To 100000'),
    )
    price = models.CharField(choices=FILTER_PRICE, max_length=60)

    def __str__(self):
        return self.price

class Product(models.Model):
    CONDITION = (('New', 'New'), ('Renewed', 'Renewed'), ('Used', 'Used'))
    STOCK = (('In Stock', 'In Stock'), ('Out of Stock', 'Out of Stock'))
    STATUS = (('Publish', 'Publish'), ('Draft', 'Draft'))

    unique_id = models.CharField(unique=True, max_length=200, null= True, blank=True)
    image = models.ImageField(upload_to='product_images/img')
    name = models.CharField(max_length=200)
    # price = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    condition = models.CharField(choices=CONDITION, max_length=100)
    information = HTMLField(null=True)
    description = HTMLField(null=True)
    # wishlisted = models.BooleanField(default=False, null=True, blank=True)
    wishlisted_by = models.ManyToManyField(User, related_name='wishlist', blank=True)
    stock = models.CharField(choices=STOCK, max_length=200)
    status = models.CharField(choices=STATUS, max_length=200)
    created_date = models.DateTimeField(default=timezone.now)


    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    filter_price = models.ForeignKey(Filter_Price, on_delete=models.CASCADE)


    def save(self, *args, **kwargs):
        if self.unique_id is None and self.created_date and self.id:
            self.unique_id = self.created_date.strftime('75%Y%m%d23') + str(self.id)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name



class Images(models.Model):
    image = models.ImageField(upload_to='product_images/img')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Images"  # This prevents Django from appending 's'

class Tag(models.Model):
    name = models.CharField(max_length=200)
    product = models.ForeignKey(Product, on_delete= models.CASCADE)



class ContactUs(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "ContactUs"  # This prevents Django from appending 's'

    def __str__(self):
        return self.email + " -------------  Subject: " + self.subject

STATUS = ((1, 'Pending'), (2, 'Order Processed'), (3, 'Order Shipped'), (4, 'Order En-route'),\
              (5, 'Order Arrived'))
class Order(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    address = models.TextField()
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    postcode = models.IntegerField()
    phone = models.IntegerField()
    email = models.EmailField()
    additional_info = models.TextField(blank=True, null=True)
    amount = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    payment_id = models.CharField(max_length=255, null=True, blank=True)
    paid = models.BooleanField(default=False, null=True)
    order_status = models.IntegerField(choices=STATUS, null=True, blank=True, default=1)

    def __str__(self):
        return self.user.username

class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.CharField(max_length=255)
    image = models.ImageField(upload_to='product_images/order_img')
    price = models.CharField(max_length=255)
    quantity = models.CharField(max_length=255)
    total = models.CharField(max_length=255)

    def __str__(self):
        return self.product[:20] + " | " + self.order.user.username + " | " + str(self.order.id)