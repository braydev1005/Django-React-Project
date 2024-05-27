from rest_framework import serializers
from rest_framework.authtoken.admin import User

from schedulerCrud.models import ScheduleEvents, AuthUser

class ScheduleEventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleEvents
        fields = '__all__'

class AuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = '__all__'