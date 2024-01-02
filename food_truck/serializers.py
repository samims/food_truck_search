from rest_framework import serializers

from food_truck.models import FoodTruck


class FoodTruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodTruck
        fields = "__all__"


class FoodTruckQuerySerializer(serializers.Serializer):
    """
    FoodTruckQuerySerializer is for validating query params of search API
    """
    lat = serializers.FloatField(max_value=90.0, allow_null=False, required=True)
    long = serializers.FloatField(max_value=180.0, allow_null=False, required=True)
    radius = serializers.IntegerField(max_value=5, allow_null=False, required=False, )
