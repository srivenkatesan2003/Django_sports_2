from rest_framework import serializers
from .models import Customer



class customer_serializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"



