from django.contrib import admin
from .models import Cateegory, Cart, MenuItem, Order, OrderItem

# Register your models here.
admin.site.register(Cateegory)
admin.site.register(Cart)
admin.site.register(MenuItem)
admin.site.register(Order)
admin.site.register(OrderItem)