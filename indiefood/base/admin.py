from django.contrib import admin

# Register your models here.
from .models import orders, tables , menu


admin.site.register(orders)
admin.site.register(tables)
admin.site.register(menu)
