from rest_framework import serializers

from food_truck.models import FoodTruck
from food_truck.utils import is_in_valid_lat_long


class FoodTruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodTruck
        exclude = ('created_at', 'updated_at',)


class FoodTruckQuerySerializer(serializers.Serializer):
    """
    FoodTruckQuerySerializer is for validating query params of search API
    """
    lat = serializers.FloatField(max_value=90.0, allow_null=False, required=True)
    long = serializers.FloatField(max_value=180.0, allow_null=False, required=True)
    radius = serializers.IntegerField(max_value=5, allow_null=False, required=False,)

    def validate(self, data):
        """
        Validate if query parameters input are within our served area
        """
        lat = data.get('lat')
        long = data.get('long')

        if not is_in_valid_lat_long(lat, long):
            raise serializers.ValidationError("We are coming to your area soon. Stay tuned!!")

        return data
