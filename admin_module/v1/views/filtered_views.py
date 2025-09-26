from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from admin_module.models import Clients, Products
from admin_module.v1.serializers.read_serializers import ClientsReadSerializer, ProductsReadSerializer, StockByProductReadSerializer
from backend_higiapp.services.pagination import StandardResultsSetPagination

""" Vistas de clientes paginados, incluyendo filtrado, búsqueda y ordenamiento """
class ClientsViewListPagination(ListAPIView):
    queryset = Clients.objects.all()
    serializer_class = ClientsReadSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAuthenticated]
    
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'status']
    search_fields = ['name', 'identification', 'address', 'phone', 'email']
    ordering = ['name']

class ProductsViewListPagination(ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsReadSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAuthenticated]
    
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'status']
    search_fields = ['name', 'code', 'description', 'price']
    ordering = ['name']

class StockByProductViewListPagination(ListAPIView):
    queryset = Products.objects.all()
    serializer_class = StockByProductReadSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAuthenticated]
    
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'status']
    search_fields = ['name', 'code', 'description']
    ordering = ['name']