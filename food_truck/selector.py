from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.measure import Distance as DistanceMeasure
from django.db.models import QuerySet

from food_truck.models import FoodTruck


class FoodTruckRepository(object):
    """
    FoodTruckRepository is created by the concept of separation of concerns
    this will access data from data source, so that we can use it from anywhere
    like - grpc, command line, rest api etc.
    And yes, it can easily be mocked
    """

    @staticmethod
    def get_food_truck_by_lat_lang_and_radius(lat: float, long: float, radius: int) -> QuerySet:
        """
        Fetches food trucks within a specified radius from the provided latitude and longitude.

        Args:
            lat (float): Latitude of the user's location.
            long (float): Longitude of the user's location.
            radius (int): Radius within which to search for food trucks (in kilometers).

        Returns:
            QuerySet: QuerySet of FoodTruck objects within the specified radius.

        """
        # TODO: we are not yet checking if the radius is also in San Francisco, suppose the
        # TODO: lat lang is in San Francisco but not the food truck, this is not coveredd

        # Create a point object from the provided coordinates
        # Assuming WGS84 coordinate system, don't ask me anything about it :-)
        # just got from internet
        user_location = Point(lat, long, srid=4326)

        # Filter food trucks within 1km radius using database spatial functions
        queryset = FoodTruck.objects.annotate(
            distance=Distance('location', user_location)
        ).filter(distance__lte=DistanceMeasure(km=radius)).order_by('distance')
        return queryset
