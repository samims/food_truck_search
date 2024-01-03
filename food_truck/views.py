from rest_framework.generics import ListAPIView

from food_truck.selector import FoodTruckRepository
from food_truck.serializers import FoodTruckSerializer, FoodTruckQuerySerializer


class FoodTruckListAPIView(ListAPIView):
    serializer_class = FoodTruckSerializer

    def get_queryset(self):
        lat, long, radius = self._validate_and_get_query_params()
        qs = FoodTruckRepository.get_food_truck_by_lat_lang_and_radius(lat, long, radius)
        return qs

    def _validate_and_get_query_params(self) -> tuple[float, float, int]:
        """
        Validates and retrieves latitude, longitude, and radius from the request query params.

        Returns:
            Tuple[float, float, int]: Latitude, longitude, and radius values.
        """
        query_serializer = FoodTruckQuerySerializer(data=self.request.query_params)
        query_serializer.is_valid(raise_exception=True)
        validated_data = query_serializer.validated_data
        lat = validated_data["lat"]
        long = validated_data["long"]
        radius = validated_data.get("radius", 1)
        return lat, long, radius
