from .models import Shipping
from rest_framework import serializers
class ShippingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipping
        fields = '__all__'