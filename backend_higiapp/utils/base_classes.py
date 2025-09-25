from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from backend_higiapp.utils.auto_fill import AutoFill

#=============================================================================
#Base ViewSet con la funcionalidad de Autollenado
#=============================================================================

class BaseAutoFillViewSet(viewsets.ModelViewSet):
    """
    ViewSet base que incluye funcionalidad de AutoFill para campos de quien crea y quien actualiza.
    """
    permission_classes = [IsAuthenticated] 
    
    def create(self, request, *args, **kwargs):
        AutoFill(request, self.request.data).AutoFillPost()
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        AutoFill(request, self.request.data).AutoFillUpdate()
        return super().update(request, *args, **kwargs) 