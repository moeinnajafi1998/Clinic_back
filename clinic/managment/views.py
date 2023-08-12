from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from .permissions import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from django.contrib.auth.models import Permission



class ClinicListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsSuperuser]
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer


class ClinicRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsSuperuser]
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer


class CategoryListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsSuperuser]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsSuperuser]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class WhareHouseListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsClinicAdmin]
    queryset = WhareHouse.objects.all()
    serializer_class = WhareHouseSerializer

class WhareHouseRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsClinicAdmin]
    queryset = WhareHouse.objects.all()
    serializer_class = WhareHouseSerializer


class ItemListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsTypical_User]
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsTypical_User]
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class UserListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsSuperuser]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ClinicAdminViewSet(APIView):
    permission_classes = [IsAuthenticated, IsSuperuser]
    def get(self, request, format=None):
        clinic_admins = User.objects.filter(user_type='Clinic_Admin')
        serializer = UserSerializer(clinic_admins, many=True)
        return Response(serializer.data, status=200)


class TypicalUserViewSet(APIView):
    permission_classes = [IsAuthenticated, IsSuperuser]
    def get(self, request, format=None):
        typical_user = User.objects.filter(user_type='Typical_User')
        serializer = UserSerializer(typical_user, many=True)
        return Response(serializer.data, status=200)

class UserRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsSuperuser]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRecognization(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
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
    

class CreatePermissionView(generics.CreateAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = [IsAuthenticated, IsSuperuser]

    def perform_create(self, serializer):
        serializer.save()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class UpdatePermissionView(generics.UpdateAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = [IsAuthenticated, IsSuperuser]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    

class DeletePermissionView(generics.DestroyAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = [IsAuthenticated, IsSuperuser]

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    

class ListPermissionsView(generics.ListAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = [IsAuthenticated, IsSuperuser]


# def initPermissions(request):
#     PermissionsForDeleteList = [1,2,3,4,5,6,7,8]