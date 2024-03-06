from django.contrib import admin
from .models import *

admin.site.register(registration)
admin.site.register(product)
admin.site.register(cart)
admin.site.register(complaints)
admin.site.register(order)
admin.site.register(orderitem)
admin.site.register(profile)
admin.site.register(profilepic)

# Register your models here.
