from rest_framework import serializers
from admin_module.models import Clients, Products

from users_module.v1.serializers.read_serializers import UsersReadLiteSerializer
from admin_module.v1.services.calculate_stock import CalculateStock

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
    stock = serializers.SerializerMethodField()
    
    class Meta:
        model = Products
        fields = [
            'id',
            'code',
            'name',
            'description',
            'price',
            'taxes',
            'value_taxes',
            'status',
            'created_by',
            'updated_by',
            'created_at',
            'updated_at',
            'stock'
        ]
        
    def get_status(self, obj):
        """ Verifica la tupla del status choices de los modelos """
        return obj.get_status_display()

    def get_taxes(self, obj):
        """ Verifica la tupla del taxes choices de los modelos """
        return obj.get_taxes_display()

    def get_stock(self, obj):
        """ Obtiene el stock del producto , mediante un group by de los status choices """
        stock = CalculateStock(obj.id).calculate_stock()

        total = int(stock[0]) - int(stock[1])

        return {
            'total': total,
            'transfer': stock[2]
        }

class StockByProductReadSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    stock = serializers.SerializerMethodField()
    updated_by = UsersReadLiteSerializer()

    class Meta:
        model = Products
        fields = [
            'id',
            'code',
            'name',
            'description',
            'status',            
            'updated_at',
            'updated_by',
            'stock'
        ]
    
    def get_status(self, obj):
        return obj.get_status_display()

    def get_taxes(self, obj):
        return obj.get_taxes_display()

    def get_stock(self, obj):
        stock = CalculateStock(obj.id).calculate_stock()
        total = int(stock[0]) - int(stock[1])

        return {
            'total': total,
            'income': stock[0],
            'outcome': stock[1],
            'transfer': stock[2]
        }
