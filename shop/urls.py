from django.urls import path
from shop import views

urlpatterns = [
    path('shops/', views.all_shop, name='all-shops'),
    path('shops/analytics/', views.shop_analytics, name='shop-analytics'),
    path('shops/products/', views.shop_products, name='shop-products'),
    path('shops/add-shop/', views.add_shop, name='add-shop')
]