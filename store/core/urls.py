from django.urls import path

from store.core.views import ProductList

app_name = 'core'

urlpatterns = [
    path('products/', ProductList.as_view(), name='product-list'),
]
