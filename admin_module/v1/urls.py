from rest_framework.routers import DefaultRouter

from admin_module.v1.views.crud_views import ClientsViewSet, ProductsViewSet

router = DefaultRouter()

""" endpoints con viewsets """
router.register(r'clients', ClientsViewSet)
router.register(r'products', ProductsViewSet)

urlpatterns = [

] + router.urls