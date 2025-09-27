from rest_framework.routers import DefaultRouter
from django.urls import path

from sales_module.v1.views.crud_views import QuotesViewSet, ItemsQuoteViewSet, ProcessViewSet
from sales_module.v1.views.filtered_views import ProcessDashboardViewListPagination, ProcessDetailView

router = DefaultRouter()

router.register(r'process', ProcessViewSet)
router.register(r'quotes', QuotesViewSet)
router.register(r'items-quote', ItemsQuoteViewSet)


urlpatterns = [
    path('process/pagination/', ProcessDashboardViewListPagination.as_view(), name='process-pagination'),
    path('process/detail/<int:id>/', ProcessDetailView.as_view(), name='process-detail'),
] + router.urls