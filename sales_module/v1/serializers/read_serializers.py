from rest_framework import serializers
from sales_module.models import Process, Quotes, ItemsQuote

from admin_module.v1.serializers.read_serializers import ClientsReadSerializer
from admin_module.v1.serializers.read_serializers import ProductsReadSerializer

from users_module.v1.serializers.read_serializers import UsersReadLiteSerializer

#===============================================================
# Dashboard Process Serializers
#===============================================================
class QuotesDashboardReadSerializer(serializers.ModelSerializer):
    client = serializers.ReadOnlyField(source='client.name')

    class Meta:
        model = Quotes
        fields = [
            'id',
            'process',
            'consecutive',
            'date_quote',
            'total',
            'status',
            'observations',
            'client',
        ]

class ProcessDashboardReadSerializer(serializers.ModelSerializer):
    quote = QuotesDashboardReadSerializer(source='quotes_process', many=True, read_only=True)
    updated_by = serializers.ReadOnlyField(source='updated_by.name')
    status = serializers.SerializerMethodField()

    class Meta:
        model = Process
        fields = [
            'id',
            'status',
            'updated_at', 
            'updated_by',
            'quote'
        ]

    def get_status(self, obj):
        return obj.get_status_display()

#===============================================================
# Dashboard Quotes Serializers
#===============================================================
class ItemsQuoteDetailReadSerializer(serializers.ModelSerializer):
    product = ProductsReadSerializer()

    class Meta:
        model = ItemsQuote
        fields = [
            'id',
            'quote',
            'process',
            'quantity',
            'subtotal',
            'total_iva',
            'total',
            'product'
        ]

class QuotesDetailReadSerializer(serializers.ModelSerializer):
    client = ClientsReadSerializer()
    items = ItemsQuoteDetailReadSerializer(source='items_quote', many=True, read_only=True)
    updated_by = UsersReadLiteSerializer()
    created_by = UsersReadLiteSerializer()

    class Meta:
        model = Quotes
        fields = [
            'id',
            'process',
            'date_quote',
            'consecutive',
            'subtotal',
            'total_iva',
            'total',
            'status',
            'observations',
            'created_by',
            'updated_by',
            'created_at',
            'updated_at',
            'client',
            'items',
        ]

class ProcessDetailReadSerializer(serializers.ModelSerializer):
    quote = QuotesDetailReadSerializer(source='quotes_process', many=True, read_only=True)
    updated_by = UsersReadLiteSerializer()
    created_by = UsersReadLiteSerializer()
    status = serializers.SerializerMethodField()
        
    class Meta:
        model = Process
        fields = [
            'id',
            'status',
            'updated_at', 
            'created_at',
            'created_by',
            'updated_by',
            'quote'
        ]

    def get_status(self, obj):
        return obj.get_status_display()