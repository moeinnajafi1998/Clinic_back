from rest_framework import generics
from .models import Clinic
from .serializers import ClinicSerializer

class ClinicListCreateView(generics.ListCreateAPIView):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer

class ClinicRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer
