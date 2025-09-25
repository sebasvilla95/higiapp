from admin_module.models import Clients
from admin_module.v1.serializers.crud_serializers import ClientsSerializer, ProductsSerializer
from admin_module.models import Products
from backend_higiapp.utils.base_classes import BaseAutoFillViewSet

class ClientsViewSet(BaseAutoFillViewSet):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer

class ProductsViewSet(BaseAutoFillViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    