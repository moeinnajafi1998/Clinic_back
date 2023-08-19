from rest_framework import serializers
from .models import *
from managment.serializers import *
class RequestSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestSession
        fields = '__all__'


class MedicalAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalAppointment
        fields = '__all__'


class RequestGoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestGoods
        fields = '__all__'


class VisitAppointmentSerializer(serializers.ModelSerializer):
    used_items = ItemSerializer(many = True)
    services = ItemSerializer(many = True)
    class Meta:
        model = VisitAppointment
        fields = '__all__'