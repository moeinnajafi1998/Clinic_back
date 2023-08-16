from rest_framework import generics
from .models import RequestSession
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from managment.permissions import * 
from rest_framework.views import APIView
from managment.models import Clinic
from rest_framework.response import Response
from .permissions import *
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView

# RequestSession Views
class RequestSessionListView(generics.ListAPIView):
    queryset = RequestSession.objects.all()
    serializer_class = RequestSessionSerializer
    permission_classes = [IsAuthenticated, IsSuperuser]

class RequestSessionCreateView(APIView):
    permission_classes = [IsAuthenticated, IsSick]
    def post(self, request, format=None):
        sick = request.user.username
        clinic = request.data.get("clinic")
        description = request.data.get("description")
        newRequestSession = RequestSession.objects.create(sick=sick,clinic=clinic,description=description)
        newRequestSession.save()
        return Response("successful", status=201)
    
class RequestSessionRetrieveView(generics.RetrieveAPIView):
    queryset = RequestSession.objects.all()
    serializer_class = RequestSessionSerializer
    permission_classes = [IsAuthenticated, IsSuperuser]

class RequestSessionUpdateView(generics.UpdateAPIView):
    queryset = RequestSession.objects.all()
    serializer_class = RequestSessionSerializer
    permission_classes = [IsAuthenticated, IsThisTypical_UserForClinic]

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_checked = not instance.is_checked
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
class RequestSessionDeleteView(generics.DestroyAPIView):
    queryset = RequestSession.objects.all()
    serializer_class = RequestSessionSerializer
    permission_classes = [IsAuthenticated, IsSuperuser]

class RequestSessionsForTypical_user(APIView):
    permission_classes = [IsAuthenticated, IsTypical_User]
    def get(self, request, *args, **kwargs):
        typical_user = request.user.username
        try: 
            clinics = Clinic.objects.filter(typical_user=typical_user)
            clinic_names = clinics.values_list('name', flat=True)
        except Clinic.DoesNotExist:
            return Response({"error": "No clinic found for this user."}, status=404)
        request_sessions = RequestSession.objects.filter(clinic__in=clinic_names)
        serializer = RequestSessionSerializer(request_sessions, many=True)  
        return Response(serializer.data, status=200)

class RequestSessionsForSick(APIView):
    permission_classes = [IsAuthenticated, IsSick]
    def get(self, request, *args, **kwargs):
        sick = request.user.username
        request_sessions = RequestSession.objects.filter(sick=sick)
        serializer = RequestSessionSerializer(request_sessions, many=True)  
        return Response(serializer.data, status=200) 
# MedicalAppointment Views
class MedicalAppointmentListView(ListAPIView):
    queryset = MedicalAppointment.objects.all()
    serializer_class = MedicalAppointmentSerializer
    permission_classes = [IsAuthenticated, IsSuperuser]

class MedicalAppointmentCreateView(APIView):
    permission_classes = [IsAuthenticated, IsThisTypical_UserForClinic_2]
    def post(self, request, format=None):
        sick = request.data.get("sick")
        typical_user = request.user.username
        clinic = request.data.get("clinic")
        nurse = request.data.get("nurse")
        description = request.data.get("description")
        date = request.data.get("date")
        time = request.data.get("time")
        medical_appointment = MedicalAppointment.objects.create(sick=sick,
                                                            clinic=clinic,
                                                            description=description,
                                                            typical_user=typical_user,
                                                            nurse=nurse,
                                                            date=date,
                                                            time=time)
        medical_appointment.save()
        return Response("successful", status=201)

class MedicalAppointmentRetrieveView(RetrieveAPIView):
    queryset = MedicalAppointment.objects.all()
    serializer_class = MedicalAppointmentSerializer
    permission_classes = [IsAuthenticated, IsSuperuser]

class MedicalAppointmentDestroyView(DestroyAPIView):
    queryset = MedicalAppointment.objects.all()
    serializer_class = MedicalAppointmentSerializer
    permission_classes = [IsAuthenticated, IsSuperuser]

class MedicalAppointmentUpdateView(generics.UpdateAPIView):
    queryset = MedicalAppointment.objects.all()
    serializer_class = MedicalAppointmentSerializer
    permission_classes = [IsAuthenticated, IsThisTypical_UserForClinic_3]

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_done = not instance.is_done
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class MedicalAppointmentsForTypical_user(APIView):
    permission_classes = [IsAuthenticated, IsTypical_User]
    def get(self, request, *args, **kwargs):
        typical_user = request.user.username
        medical_appointments = MedicalAppointment.objects.filter(typical_user=typical_user)
        serializer = MedicalAppointmentSerializer(medical_appointments, many=True)  
        return Response(serializer.data, status=200)
    
class MedicalAppointmentsForSick(APIView):
    permission_classes = [IsAuthenticated, IsSick]
    def get(self, request, *args, **kwargs):
        sick = request.user.username
        medical_appointments = MedicalAppointment.objects.filter(sick=sick)
        serializer = MedicalAppointmentSerializer(medical_appointments, many=True)  
        return Response(serializer.data, status=200)
# RequestGoods Views
class RequestGoodsListView(ListAPIView):
    queryset = RequestGoods.objects.all()
    serializer_class = RequestGoodsSerializer
    permission_classes = [IsAuthenticated, IsSuperUserOrWhareHouseKeeper]

class RequestGoodsForTypical_user(APIView):
    permission_classes = [IsAuthenticated, IsTypical_User]
    def get(self, request, *args, **kwargs):
        typical_user = request.user.username
        rgs = RequestGoods.objects.filter(typical_user=typical_user)
        serializer = RequestGoodsSerializer(rgs, many=True)  
        return Response(serializer.data, status=200)

class RequestGoodsCreateView(APIView):
    permission_classes = [IsAuthenticated, IsThisTypical_UserForClinic_2]
    def post(self, request, format=None):
        item = request.data.get("item")
        typical_user = request.user.username
        clinic = request.data.get("clinic")
        number = int(request.data.get("number"))
        description = request.data.get("description")
        rg = RequestGoods.objects.create(item=item,
                                        clinic=clinic,
                                        description=description,
                                        typical_user=typical_user,
                                        number=number)
        rg.save()
        return Response("successful", status=201)

class RequestGoodsRetrieveView(RetrieveAPIView):
    queryset = RequestGoods.objects.all()
    serializer_class = RequestGoodsSerializer
    permission_classes = [IsAuthenticated, IsSuperuser]

class RequestGoodsDestroyView(DestroyAPIView):
    queryset = RequestGoods.objects.all()
    serializer_class = RequestGoodsSerializer
    permission_classes = [IsAuthenticated, IsSuperuser]

class RequestGoodsUpdateView(generics.UpdateAPIView):
    queryset = RequestGoods.objects.all()
    serializer_class = RequestGoodsSerializer
    permission_classes = [IsAuthenticated, IsWarehouse_Keeper]

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_done = not instance.is_done
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)