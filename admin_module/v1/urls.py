from rest_framework.routers import DefaultRouter
from django.urls import path

from admin_module.v1.views.crud_views import ClientsViewSet, ProductsViewSet
from admin_module.v1.views.filtered_views import ClientsViewListPagination, ProductsViewListPagination

router = DefaultRouter()

""" endpoints con viewsets """
router.register(r'clients', ClientsViewSet)
router.register(r'products', ProductsViewSet)

urlpatterns = [
    path('clients/pagination/', ClientsViewListPagination.as_view(), name='clients-pagination'),
    path('products/pagination/', ProductsViewListPagination.as_view(), name='products-pagination'),
] + router.urls