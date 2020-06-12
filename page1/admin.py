from django.contrib import admin
from .models import customer,product,client,contact,cart
# Register your models here.
admin.site.register(customer)
admin.site.register(product)
admin.site.register(client)
admin.site.register(contact)
admin.site.register(cart)