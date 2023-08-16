from rest_framework import generics
from .models import RequestSession
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from managment.permissions import * 
from rest_framework.views import APIView
from managment.models import Clinic
from rest_framework.response import Response
from .permissions import IsThisTypical_UserForClinic


class RequestSessionListView(generics.ListAPIView):
    queryset = RequestSession.objects.all()
    serializer_class = RequestSessionSerializer
    permission_classes = [IsAuthenticated, IsSuperuser]

class RequestSessionCreateView(generics.CreateAPIView):
    queryset = RequestSession.objects.all()
    serializer_class = RequestSessionSerializer
    permission_classes = [IsAuthenticated, IsSick]


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