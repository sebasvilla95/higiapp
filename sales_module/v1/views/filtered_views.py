from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from sales_module.models import Process
from sales_module.v1.serializers.read_serializers import ProcessDashboardReadSerializer, ProcessDetailReadSerializer
from backend_higiapp.services.pagination import StandardResultsSetPagination


class ProcessDashboardViewListPagination(ListAPIView):
    queryset = Process.objects.all()
    serializer_class = ProcessDashboardReadSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAuthenticated]
    
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'status', 'updated_by']
    search_fields = ['quotes_process__client__name', 'quotes_process__consecutive']
    ordering = ['-updated_at']

class ProcessDetailView(RetrieveAPIView):
    queryset = Process.objects.select_related('updated_by', 'created_by').prefetch_related('quotes_process', 'quotes_process__items_quote').all()
    serializer_class = ProcessDetailReadSerializer
    permission_classes = [IsAuthenticated]

    lookup_field = 'id'
