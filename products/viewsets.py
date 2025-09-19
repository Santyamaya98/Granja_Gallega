# products/viewsets.py
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import IsSupplier
from .serializers import ProductsSerializer, ProdcutsPromoSerializer
from .models import SuppliersProductsModel, PromosModel


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = SuppliersProductsModel.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    
    
class PromoViewSet(viewsets.ModelViewSet):
    queryset = PromosModel.objects.all()
    serializer_class = ProdcutsPromoSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]