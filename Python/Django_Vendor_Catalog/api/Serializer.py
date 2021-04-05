from rest_framework import serializers
from catalog.models import Vendor, Product  # importing the models from web application


# Serializer to Product Model
class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


# Serializer to Vendor Model
class VendorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vendor
        fields = '__all__'


# Serializer to Product Model with complete vendor information used get list method
class ProductListSerializer(serializers.ModelSerializer):

    vendor = VendorSerializer()

    class Meta:
        model = Product
        fields = '__all__'
