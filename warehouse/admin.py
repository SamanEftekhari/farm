from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import *

admin.site.register(Warehouse)
admin.site.register(WarehouseLocation)
admin.site.register(Stock)
admin.site.register(StockTransaction)
