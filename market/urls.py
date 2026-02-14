from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('portfolio/manage/', views.manage_portfolio, name='manage_portfolio'),
    path('asset/<slug:slug>/', views.asset_detail, name='asset_detail'),
    path('api/assets/', views.api_assets, name='api_assets'),
    path('api/asset/<slug:slug>/candles', views.api_candles, name='api_candles'),
    path('api/update/', views.api_update, name='api_update'),
]
