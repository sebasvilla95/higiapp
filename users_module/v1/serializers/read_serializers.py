from rest_framework import serializers
from users_module.models import Users

class UsersReadSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    is_superuser = serializers.SerializerMethodField()

    class Meta:
        model = Users
        fields = ['id', 'first_name', 'last_name', 'email', 'status', 'is_superuser']


    def get_status(self, obj):
        return obj.get_status_display()

    def get_is_superuser(self, obj):
        return obj.is_superuser

class UsersReadLiteSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()

    class Meta:
        model = Users
        fields = ['id', 'name', 'status']
        
    def get_status(self, obj):
        return obj.get_status_display()

    def get_name(self, obj):
        return obj.first_name + ' ' + obj.last_name