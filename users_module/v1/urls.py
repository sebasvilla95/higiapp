from django.urls import path

from rest_framework_simplejwt import views as jwt_views

from users_module.v1.views import crud_views


urlpatterns = [ 
    path('login/', crud_views.Login.as_view(), name='Inicio de sesión'),
    path('profile/', crud_views.UserProfile.as_view(), name='Perfil de usuario'),
    path('change-password/', crud_views.PasswordChangeView.as_view(), name='Cambiar contraseña'),
    path('user/<int:pk>/', crud_views.UserViewDetail.as_view(), name='detalle de usuario'),
    path('user/', crud_views.UserViewList.as_view(), name='Lista de usuarios'),
    path('user-pagination/', crud_views.UserViewListPagination.as_view(), name='Lista de usuarios paginada'),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]