from rest_framework import generics
from store.products.models import Product
from store.products.serializers import ProductSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # authentication_classes = [SessionAuthentication]
    # permission_classes = (IsAuthenticated, )


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # authentication_classes = [SessionAuthentication]
    # permission_classes = (IsAuthenticated, )
