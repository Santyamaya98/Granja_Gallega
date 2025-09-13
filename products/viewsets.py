# products/viewsets.py
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import IsSupplier
from .serializers import ProductsSerializer
from .models import SuppliersProductsModel
from Suppliers.models import SuppliersModel
from django.shortcuts import get_object_or_404


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = SuppliersProductsModel.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = [IsAuthenticated, IsSupplier]

    
    @action(detail=True, methods=['GET','PUT'], permission_classes=[IsAuthenticated, IsAdminUser], url_path='edit-product')
    def edit_product(self, request, supplier_pk, product_pk):
        if request.method == 'GET':
            try:
                # ✅ Get the product using the ID from the URL
                supplier = get_object_or_404(SuppliersModel, pk=supplier_pk, approved=True)
                products = SuppliersProductsModel.objects.filter(supplier=supplier)
            except SuppliersProductsModel.DoesNotExist:
                return Response({'detail': 'Products not found.'}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = ProductsSerializer(products, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save() 
            return Response({'detail': 'Products list'}, status=status.HTTP_200_OK)  

        if request.method == 'PUT':
            try:
                supplier = get_object_or_404(SuppliersModel, pk=supplier_pk, approved=True)
                product = SuppliersProductsModel.objects.filter(pk=product_pk)
                # ✅ Update the product using partial=True to allow partial updates
            except SuppliersProductsModel.DoesNotExist:
                return Response({'detail': 'Product not found.'}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = ProductsSerializer(product, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()   
            return Response(serializer.data, {'detail': 'product updated'}, status=status.HTTP_201_CREATED)
    
