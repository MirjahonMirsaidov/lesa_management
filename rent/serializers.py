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
        fields = ('id', 'name', 'type', 'price', 'quantity', 'image')


class RentedItemSerializer(serializers.ModelSerializer):
    item = ItemSerializer()

    class Meta:
        model = RentedItem
        fields = ('item', 'quantity', 'record')


class RentedItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentedItem
        fields = '__all__'


class RentSerializer(serializers.ModelSerializer):
    rented_item = RentedItemSerializer(required=False, many=True)
    rentee = RenteeSerializer(required=False)
    renter = RenterSerializer(required=False)
    entered_by = RenterSerializer(required=False)

    class Meta:
        model = Rent
        fields = ('id', 'rented_date', 'rentee', 'renter', 'entered_by', 'rented_item', 'total_cost',
                  'paid', 'closed_date')


class RentCreateSerializer(serializers.ModelSerializer):
    rented_item = serializers.ListField()

    class Meta:
        model = Rent
        fields = ('rentee', 'renter', 'entered_by', 'total_cost', 'paid', 'closed_date', 'rented_item')

    def create(self, validated_data):
        rentee = validated_data.get('rentee')
        renter = validated_data.get('renter')
        entered_by = validated_data.get('entered_by')
        total_cost = validated_data.get('total_cost')
        paid = validated_data.get('paid')
        closed_date = validated_data.get('closed_date')
        rented_items = validated_data.get('rented_item')
        rent = Rent.objects.create(
            rentee=rentee,
            renter=renter,
            entered_by=entered_by,
            total_cost=total_cost,
            paid=paid,
            closed_date=closed_date,
        )
        for ritem in rented_items:
            ritem_ser = RentedItemCreateSerializer(data={'item': ritem.get('item'),
                                                   'quantity': ritem.get('quantity'), 'record': rent.id})
            if ritem_ser.is_valid():
                ritem_ser.save()
        return rent
