from django.contrib import admin

from rent.models import Rent, Item, Type, RentedItem


admin.site.register(Rent)
admin.site.register(Item)
admin.site.register(RentedItem)
admin.site.register(Type)
