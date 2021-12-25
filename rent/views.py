from rest_framework import generics

from rent.models import Rent
from rent.serializers import RentSerializer


class RentListView(generics.ListAPIView):
    queryset = Rent.objects.all()
    serializer_class = RentSerializer