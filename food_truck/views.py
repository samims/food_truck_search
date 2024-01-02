from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.measure import Distance as DistanceMeasure
from rest_framework.generics import ListAPIView

from food_truck.models import FoodTruck
from food_truck.serializers import FoodTruckSerializer, FoodTruckQuerySerializer


class FoodTruckListAPIView(ListAPIView):
    serializer_class = FoodTruckSerializer

    def get_queryset(self):
        # validate query params
        query_serializer = FoodTruckQuerySerializer(data=self.request.query_params)
        query_serializer.is_valid(raise_exception=True)
        validated_data = query_serializer.validated_data

        lat = validated_data["lat"]
        long = validated_data["long"]
        radius = validated_data.get("radius", 1)

        # Create a point object from the provided coordinates
        # Assuming WGS84 coordinate system, don't ask me anything about it :-)
        # just got from internet

        user_location = Point(lat, long, srid=4326)

        # Filter food trucks within 1km radius using database spatial functions
        queryset = FoodTruck.objects.annotate(
            distance=Distance('location', user_location)
        ).filter(distance__lte=DistanceMeasure(km=radius)).order_by('distance')

        return queryset
