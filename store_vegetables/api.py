from rest_framework import viewsets, permissions
from .serializers import *


class VegetablesViewSet(viewsets.ModelViewSet):
    queryset = Vegetable.objects.all()
    http_method_names = ['get']
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = VegetablesSerializer
