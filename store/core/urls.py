from django.urls import path

from store.core.views import ProductList, ProductDetail

app_name = 'core'

urlpatterns = [
    path('products/', ProductList.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
]
