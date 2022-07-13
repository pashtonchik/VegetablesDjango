from rest_framework import serializers
from .models import *


class VegetablesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vegetable
        fields = '__all__'
