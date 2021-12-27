from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from rent.models import Rent
from rent.serializers import RentSerializer, RentCreateSerializer, RentedItemSerializer


class RentListCreateView(generics.ListCreateAPIView):
    serializer_class = RentSerializer

    def get_queryset(self):
        return Rent.objects.order_by('-id')

    def post(self, request):
        rent = RentCreateSerializer(data=request.data)
        if rent.is_valid():
            rent.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(rent.errors, status=status.HTTP_400_BAD_REQUEST)


class RentDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RentSerializer
    queryset = Rent.objects.all()

