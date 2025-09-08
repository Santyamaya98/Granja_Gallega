from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.models import User
from .models import SuppliersModel
from .serializers import SuppliersSerializer

class SuppliersViewSet(viewsets.ModelViewSet):
    queryset = SuppliersModel.objects.all()
    serializer_class = SuppliersSerializer
    permission_classes = [IsAuthenticated]
    auth_permmissions = [IsAdminUser]
    def get_queryset(self):
        # Return only suppliers associated with the authenticated user
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically associate the supplier with the authenticated user
        serializer.save(user=self.request.user)

    def add_supplier(self, request):
        supplier = self.get_object()
        serializer = SuppliersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(supplier=supplier)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list_suppliers(self, request):
        supplier = self.get_objects.all()
        serializer = SuppliersSerializer(supplier, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
    @action(detail=True, methods=['POST','GET'], permission_classes= auth_permmissions)
    def suppliers(self, request, pk):
        if request.method == 'POST':
            return self.add_supplier(request)
        elif request.method == 'GET':    
            return self.list_suppliers(request)
