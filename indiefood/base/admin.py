from django.contrib import admin

# Register your models here.
from .models import orders, tables


admin.site.register(orders)
admin.site.register(tables)
