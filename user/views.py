from rest_framework import generics

from user.models import Rentee
from user.serializers import RenteeSerializer


class RenteeListCreateView(generics.ListCreateAPIView):
    queryset = Rentee.objects.all()
    serializer_class = RenteeSerializer


class RenteeUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rentee.objects.all()
    serializer_class = RenteeSerializer
