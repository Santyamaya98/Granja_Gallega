from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.models import User
from .models import SuppliersModel
from .serializers import SuppliersSerializer

class SuppliersViewSet(viewsets.ModelViewSet):

    queryset = SuppliersModel.objects.all()
    serializer_class = SuppliersSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    