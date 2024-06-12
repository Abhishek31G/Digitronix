from django.contrib import admin
from .models import *

class ImagesTabularInline(admin.TabularInline):
    model = Images 

class TagTabularInline(admin.TabularInline):
    model = Tag

class ProductAdmin(admin.ModelAdmin):
    inlines = [ImagesTabularInline, TagTabularInline]
    # list_display=['wishlisted','name']


class OrderItemTubularInline(admin.TabularInline):
    model = OrderItem

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemTubularInline]
    list_display=['firstname','phone' ,'email','payment_id','paid','date'] 
    search_fields = ['firstname', 'email', 'payment']


admin.site.register(Images)
admin.site.register(Tag)

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(Filter_Price)
admin.site.register(ContactUs)
admin.site.register(Product,ProductAdmin)

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
