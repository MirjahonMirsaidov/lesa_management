from rest_framework import serializers
from django.contrib.auth.models import User

from user.models import Rentee


class RenteeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rentee
        fields = '__all__'


class RenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')
