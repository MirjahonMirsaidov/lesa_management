from rest_framework import serializers

from rent.models import Rent, Item, Type, RentedItem
from user.serializers import RenteeSerializer, RenterSerializer


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    type = TypeSerializer()

    class Meta:
        model = Item
        fields = ('name', 'type', 'price', 'quantity', 'image')


class RentedItemSerializer(serializers.ModelSerializer):
    item = ItemSerializer()

    class Meta:
        model = RentedItem
        fields = ('item', 'quantity')


class RentSerializer(serializers.ModelSerializer):
    rented_item = RentedItemSerializer(many=True)
    rentee = RenteeSerializer()
    renter = RenterSerializer()
    entered_by = RenterSerializer()

    class Meta:
        model = Rent
        fields = ('rentee', 'renter', 'entered_by', 'rented_item', 'total_cost', 'paid', 'rented_date', 'closed_date')
