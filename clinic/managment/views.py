from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from .permissions import *

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


class UserRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsSuperuser]
    queryset = User.objects.all()
    serializer_class = UserSerializer
