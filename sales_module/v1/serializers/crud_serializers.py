from rest_framework import serializers
from sales_module.models import Quotes, ItemsQuote, Process

class ProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Process
        fields = '__all__'

class QuotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quotes
        fields = '__all__'

class ItemsQuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemsQuote
        fields = '__all__'