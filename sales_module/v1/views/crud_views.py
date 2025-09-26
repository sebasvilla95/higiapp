from sales_module.models import Quotes, ItemsQuote, Process
from sales_module.v1.serializers.crud_serializers import QuotesSerializer, ItemsQuoteSerializer, ProcessSerializer
from backend_higiapp.utils.base_classes import BaseAutoFillViewSet


class ProcessViewSet(BaseAutoFillViewSet):
    queryset = Process.objects.all()
    serializer_class = ProcessSerializer
    
class QuotesViewSet(BaseAutoFillViewSet):
    queryset = Quotes.objects.all()
    serializer_class = QuotesSerializer

class ItemsQuoteViewSet(BaseAutoFillViewSet):
    queryset = ItemsQuote.objects.all()
    serializer_class = ItemsQuoteSerializer
