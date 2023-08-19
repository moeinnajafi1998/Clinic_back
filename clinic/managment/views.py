from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from .permissions import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from django.contrib.auth.models import Permission
from django.contrib.auth.hashers import make_password


# APIs for Clinic Model
class ClinicListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer

class ClinicCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, IsSuperuser]
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer

class ClinicRetrieveView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated, IsSuperuser]
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer

class ClinicUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated, IsSuperuser]
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer

class ClinicDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated, IsSuperuser]
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer
# APIs for Category Model
class CategoryListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated, IsSuperuser]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, IsSuperuser]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieveView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated, IsSuperuser]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated, IsSuperuser]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated, IsSuperuser]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
# APIs for WhareHouse Model
class WarehouseListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated, IsSuperuser]
    queryset = WhareHouse.objects.all()
    serializer_class = WhareHouseSerializer

class WarehouseCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, IsSuperuser]
    queryset = WhareHouse.objects.all()
    serializer_class = WhareHouseSerializer

class WarehouseRetrieveView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated, IsSuperuser]
    queryset = WhareHouse.objects.all()
    serializer_class = WhareHouseSerializer

class WarehouseUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated, IsSuperuser]
    queryset = WhareHouse.objects.all()
    serializer_class = WhareHouseSerializer

class WarehouseDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated, IsSuperuser]
    queryset = WhareHouse.objects.all()
    serializer_class = WhareHouseSerializer
# APIs for Item Model
class ItemListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated,IsSuperuser]
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemListViewDistinct(generics.ListAPIView):
    permission_classes = [IsAuthenticated,IsNurse]
    def get_queryset(self):
        queryset = Item.objects.distinct('field_name')
        return queryset

class ItemNamesListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated,IsTypical_User]
    queryset = Item.objects.all()
    serializer_class = ItemSerializer2

class ItemCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, IsSuperuser]
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemRetrieveView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated, IsSuperuser]
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated, IsSuperuser]
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated, IsSuperuser]
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
# APIs for Service Model
class ServiceListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated,IsSuperuser]
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, IsSuperuser]
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceRetrieveView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated, IsSuperuser]
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated, IsSuperuser]
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated, IsSuperuser]
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
# APIs for Permission Model
class ListPermissionsView(generics.ListAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = [IsAuthenticated, IsSuperuser]

class CreatePermissionView(generics.CreateAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = [IsAuthenticated, IsSuperuser]

class PermissionRetrieveView(generics.RetrieveAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer 
    permission_classes = [IsAuthenticated, IsSuperuser]

class UpdatePermissionView(generics.UpdateAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = [IsAuthenticated, IsSuperuser]
    
class DeletePermissionView(generics.DestroyAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = [IsAuthenticated, IsSuperuser]
# APIs for User Model
class UserListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated, IsSuperuser]
    queryset = User.objects.all()
    serializer_class = UserListSerializer

class ClinicAdminViewSet(APIView):
    permission_classes = [IsAuthenticated, IsSuperuser]
    def get(self, request, format=None):
        clinic_admins = User.objects.filter(user_type='Clinic_Admin')
        serializer = UserListSerializer(clinic_admins, many=True)
        return Response(serializer.data, status=200)

class TypicalUserViewSet(APIView):
    permission_classes = [IsAuthenticated, IsSuperuser]
    def get(self, request, format=None):
        typical_user = User.objects.filter(user_type='Typical_User')
        serializer = UserListSerializer(typical_user, many=True)
        return Response(serializer.data, status=200)

class NurseViewSet(APIView):
    permission_classes = [IsAuthenticated, IsSuperuser]
    def get(self, request, format=None):
        Nurse = User.objects.filter(user_type='Nurse')
        serializer = UserListSerializer(Nurse, many=True)
        return Response(serializer.data, status=200)

class SickViewSet(APIView):
    permission_classes = [IsAuthenticated, IsSuperuser]
    def get(self, request, format=None):
        Sick = User.objects.filter(user_type='Sick')
        serializer = UserListSerializer(Sick, many=True)
        return Response(serializer.data, status=200)

class WarehouseKeeperViewSet(APIView):
    permission_classes = [IsAuthenticated, IsSuperuser]
    def get(self, request, format=None):
        Warehouse_Keeper = User.objects.filter(user_type='Warehouse_Keeper')
        serializer = UserListSerializer(Warehouse_Keeper, many=True)
        return Response(serializer.data, status=200)
    
class FinancialManagerViewSet(APIView):
    permission_classes = [IsAuthenticated, IsSuperuser]
    def get(self, request, format=None):
        Financial_Manager = User.objects.filter(user_type='Financial_Manager')
        serializer = UserListSerializer(Financial_Manager, many=True)
        return Response(serializer.data, status=200)

class CreateUser(generics.CreateAPIView):
    serializer_class = CreateUserSerializer
    permission_classes = [IsAuthenticated, IsSuperuser]
    def perform_create(self, serializer):
        instance = serializer.save()
        hashed_password = make_password(instance.password)
        instance.password = hashed_password
        instance.save()

class UserRetrieveView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer 
    permission_classes = [IsAuthenticated, IsSuperuser]

class UpdateUserView(generics.UpdateAPIView):
    serializer_class = CreateUserSerializer
    permission_classes = [IsAuthenticated, IsSuperuser]
    queryset = User.objects.all()

    def perform_update(self, serializer):
        instance = serializer.save()
        hashed_password = make_password(instance.password)
        instance.password = hashed_password
        instance.save()

class DeleteUserView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated, IsSuperuser]
    queryset = User.objects.all()
    serializer_class = UserListSerializer
# other APIs
class UserRecognization(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    def retrieve(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            return self.retrieve_response(user)
        else:
            return Response({'message': 'User is not authenticated'}, status=401)
    def retrieve_response(self, user):
        serialized_user = self.get_serializer(user)
        return Response(serialized_user.data)
    

class TestToken(APIView):
    permission_classes = [IsAuthenticated,]
    def get(self, request):
        return Response(200)