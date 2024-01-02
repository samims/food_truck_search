from django.urls import path

from .views import FoodTruckListAPIView


app_name = "food_truck"

urlpatterns = [
    path("search", FoodTruckListAPIView.as_view())
]
