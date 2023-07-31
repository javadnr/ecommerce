from django.shortcuts import render
from .serializers import ProductSerializer, UserSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from stuff.models import Product
from django.contrib.auth.models import User


class ProductList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class ProductDetail(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdate(RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDelete(RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductEdit(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class UserEdit(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
