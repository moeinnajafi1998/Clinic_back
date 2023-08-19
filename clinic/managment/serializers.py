from rest_framework import serializers
from .models import *
from django.contrib.auth.models import Permission
from rest_framework import serializers

class ClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
class WhareHouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhareHouse
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class ItemSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['name',]

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'

class UserListSerializer(serializers.ModelSerializer):
    user_permissions = PermissionSerializer(many=True)
    class Meta:
        model = User
        fields = ['id','username','is_superuser','user_type','user_permissions','image','is_staff']

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','password','is_superuser','user_type','user_permissions','image','is_staff']
        extra_kwargs = {
            'password': {'write_only': True},
        }