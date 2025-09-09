from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import ProductsSerializer
from .models import SuppliersProductsModel

class ProductsViewSet(viewsets.ModelViewSet):
    queryset = SuppliersProductsModel.objects.all()
    serializer_class = ProductsSerializer

    permission_classes = [IsAuthenticated, IsAdminUser]
