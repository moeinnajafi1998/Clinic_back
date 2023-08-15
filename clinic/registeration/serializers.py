from rest_framework import serializers
from .models import RequestSession

class RequestSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestSession
        fields = '__all__'
