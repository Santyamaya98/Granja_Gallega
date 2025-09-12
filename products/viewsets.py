from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import IsSupplierOrAdmin
from .serializers import ProductsSerializer
from .models import SuppliersProductsModel

class ProductsViewSet(viewsets.ModelViewSet):
    queryset = SuppliersProductsModel.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = [IsAuthenticated, IsSupplierOrAdmin]

    @action(detail=True, methods=['put'], permission_classes=[IsAuthenticated, IsSupplierOrAdmin], url_path='edit-product')
    def edit_product(self, request, product_id):
        try:
            # ✅ Get the product using the ID from the URL
            product = SuppliersProductsModel.objects.get(id=product_id)
        except SuppliersProductsModel.DoesNotExist:
            return Response({'detail': 'Product not found.'}, status=status.HTTP_404_NOT_FOUND)

        # ✅ Update the product using partial=True to allow partial updates
        serializer = ProductsSerializer(product, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()   

        return Response(serializer.data, status=status.HTTP_200_OK)