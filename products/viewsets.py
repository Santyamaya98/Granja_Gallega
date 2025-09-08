from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import ProductsSerializer
from .models import SuppliersProductsModel

class ProductsViewSet(viewsets.ModelViewSet):
    queryset = SuppliersProductsModel.objects.all()
    serializer_class = ProductsSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Return only products associated with the authenticated user's suppliers
        user = self.request.user
        return self.queryset.filter(supplier__user=user)

    def perform_create(self, serializer):
        # Automatically associate the product with the authenticated user's supplier
        serializer.save(supplier=self.request.user.supplier)

    def add_product(self, request, pk):
        product = self.get_object()
        serializer = ProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(product=product)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)      
    def list_products(self, request, pk):   
        product = self.get_object()
        serializer = ProductsSerializer(product, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['POST','GET'], permission_classes=[IsAuthenticated]) 
    def products(self, request, pk):
        if request.method == 'POST':
            return self.add_product(request, pk)
        elif request.method == 'GET':    
            return self.list_products(request, pk)