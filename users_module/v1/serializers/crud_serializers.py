from django.contrib.auth import get_user_model

from rest_framework import serializers

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users_module.models import Users

class UsersSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = get_user_model()
        fields = ['id', 'password', 'email', 'first_name', 'last_name', 'status', 'is_superuser']
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)
    
    def update(self, instance, validated_data): 
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)  
        
        if password:
            user.set_password(password)
            user.save()
            
        return user
    
class UserLiteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = get_user_model()
        fields = ['id', 'password', 'email', 'first_name', 'last_name', 'status']
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)
    
    def update(self, instance, validated_data): 
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)  
        
        if password:
            user.set_password(password)
            user.save()
            
        return user   

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['id'] = user.id
        token['status'] = user.status
        token['is_superuser'] = user.is_superuser

        return token   
    
class CustomTokenObtainPairExternalSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['company_id'] = user.client.id if user.client else None
        token['status'] = user.status

        return token

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'first_name', 'last_name', 'image', 'email']
        read_only_fields = ['id', 'email']  # Email should not be changed through profile update

class PasswordChangeSerializer(serializers.Serializer):
    current_password = serializers.CharField(required=True, write_only=True)
    new_password = serializers.CharField(required=True, write_only=True)
    confirm_password = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError({"new_password": "Password fields didn't match"})
        return data

    def validate_current_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError("Current password is incorrect")
        return value