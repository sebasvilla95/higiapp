from rest_framework.routers import DefaultRouter

from sales_module.v1.views.crud_views import QuotesViewSet, ItemsQuoteViewSet, ProcessViewSet

router = DefaultRouter()

router.register(r'process', ProcessViewSet)
router.register(r'quotes', QuotesViewSet)
router.register(r'items-quote', ItemsQuoteViewSet)


urlpatterns = router.urls