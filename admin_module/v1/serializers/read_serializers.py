from rest_framework import serializers
from admin_module.models import Clients, Products

from users_module.v1.serializers.read_serializers import UsersReadLiteSerializer

class ClientsReadSerializer(serializers.ModelSerializer):
    created_by = UsersReadLiteSerializer()
    updated_by = UsersReadLiteSerializer()
    status = serializers.SerializerMethodField()

    class Meta:
        model = Clients
        fields = '__all__'

    def get_status(self, obj):
        return obj.get_status_display()

class ProductsReadSerializer(serializers.ModelSerializer):
    created_by = UsersReadLiteSerializer()
    updated_by = UsersReadLiteSerializer()
    status = serializers.SerializerMethodField()
    taxes = serializers.SerializerMethodField()
    
    class Meta:
        model = Products
        fields = '__all__'
        
    def get_status(self, obj):
        return obj.get_status_display()

    def get_taxes(self, obj):
        return obj.get_taxes_display()