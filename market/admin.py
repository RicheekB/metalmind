from django.contrib import admin
from .models import Asset, PriceSnapshot, PriceCandle

admin.site.register(Asset)
admin.site.register(PriceSnapshot)
admin.site.register(PriceCandle)
