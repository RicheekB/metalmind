from django.contrib import admin
from .models import Asset, PriceSnapshot, PriceCandle, PortfolioItem

admin.site.register(Asset)
admin.site.register(PriceSnapshot)
admin.site.register(PriceCandle)
admin.site.register(PortfolioItem)
