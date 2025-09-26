from rest_framework.routers import DefaultRouter
from django.urls import path

from admin_module.v1.views.crud_views import ClientsViewSet, ProductsViewSet, ManageStockViewSet
from admin_module.v1.views.filtered_views import ClientsViewListPagination, ProductsViewListPagination, StockByProductViewListPagination

router = DefaultRouter()

""" endpoints con viewsets """
router.register(r'clients', ClientsViewSet)
router.register(r'products', ProductsViewSet)
router.register(r'manage-stock', ManageStockViewSet)

urlpatterns = [
    path('clients/pagination/', ClientsViewListPagination.as_view(), name='clients-pagination'),
    path('products/pagination/', ProductsViewListPagination.as_view(), name='products-pagination'),
    path('stock-by-product/pagination/', StockByProductViewListPagination.as_view(), name='stock-by-product-pagination'),
] + router.urls