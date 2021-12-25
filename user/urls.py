from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from user.views import (
    RenteeListCreateView,
    RenteeUpdateDeleteView
)


urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('rentee/<int:pk>', RenteeUpdateDeleteView.as_view()),
    path('rentee/', RenteeListCreateView.as_view())
]