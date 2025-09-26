from rest_framework import serializers
from admin_module.models import Clients, Products, ManageStock

class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = '__all__'

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'

class ManageStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManageStock
        fields = '__all__'