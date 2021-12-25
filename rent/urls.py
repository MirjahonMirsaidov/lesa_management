from django.urls import path

from rent.views import RentListView


urlpatterns = [
    path('list/', RentListView.as_view())
]