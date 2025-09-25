from datetime import datetime

from django.contrib.auth import authenticate

from django.contrib.sessions.models import Session

from rest_framework import generics, status
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from users_module.permissions import IsSuperUser

from backend_higiapp.services import pagination

from users_module.v1.serializers.crud_serializers import UsersSerializer, CustomTokenObtainPairSerializer, ProfileSerializer, UserLiteSerializer, PasswordChangeSerializer

from users_module.models import Users

#=======================
#Vistas de autenticación
#=======================
class Login(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    
    def post(self, request, *args, **kwargs):
        username = request.data.get('email', '')
        password = request.data.get('password','')
        user = authenticate(
            username=username,
            password=password
        )
     
        if user and user.status == 1:
            login_serializer = self.serializer_class(data=request.data)
            if login_serializer.is_valid():
                user_serializer = UserLiteSerializer(user) 
                all_sessions = Session.objects.filter(expire_date__gte=datetime.now())
                if all_sessions.exists():
                    for session in all_sessions:
                        session_data = session.get_decoded()
                        if user.id == int(session_data.get('_auth_user_id')):
                            session.delete()
                return Response(
                    {
                        'token' : login_serializer.validated_data.get('access'),
                        'refresh' : login_serializer.validated_data.get('refresh'),
                        'user' : user_serializer.data,
                    }, status=status.HTTP_200_OK)
        return Response(
            {
                'error' : 'Contraseña o nombre de usuario incorrectos'
            }, status=status.HTTP_400_BAD_REQUEST) 

#====================================================
#Vistas de CRUD de usuarios
#====================================================

class UserViewList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [IsAuthenticated, IsSuperUser]
    
    def get(self, request, *args, **kwargs):
        
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        
        return self.create(request, *args, **kwargs)
            
class UserViewListPagination(ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    pagination_class = pagination.StandardResultsSetPagination
    permission_classes = [IsAuthenticated, IsSuperUser]
    
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id']
    search_fields = ['first_name', 'last_name', 'email']
    ordering = ['first_name']
            
class UserViewDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [IsAuthenticated, IsSuperUser]
    
    def get(self, request, *args, **kwargs):
        
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        
        return self.destroy(request, *args, **kwargs)
    
class UserProfile(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Users.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        user_pk = request.user.id
        print(user_pk)
        user = Users.objects.get(id = user_pk)
        serializer = ProfileSerializer(user)
        return Response(serializer.data)
    
    def patch(self, request, format=None):
        user_pk = request.user.id
        user = Users.objects.get(id = user_pk)
        serializer = ProfileSerializer(user, data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PasswordChangeView(generics.GenericAPIView):
    serializer_class = PasswordChangeSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = request.user
            user.set_password(serializer.validated_data['new_password'])
            user.save()
            return Response({"message": "Password changed successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
