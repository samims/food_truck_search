from django.test import TestCase
from django.conf import settings

from food_truck.utils import is_in_valid_lat_long


class TestIsValidLatLong(TestCase):

    def test_valid_lat_long(self):
        # Define latitude and longitude within the valid boundary
        valid_lat = 37.7749
        valid_long = -122.6

        # Check if the provided lat-long is within the valid boundary
        result = is_in_valid_lat_long(valid_lat, valid_long)

        # Assert that the result is True for a valid lat-long
        self.assertTrue(result)

    def test_invalid_lat_long(self):
        # Define latitude and longitude outside the valid boundary
        invalid_lat = 40.7128
        invalid_long = -74.0060

        # Check if the provided lat-long is within the valid boundary
        result = is_in_valid_lat_long(invalid_lat, invalid_long)

        # Assert that the result is False for an invalid lat-long
        self.assertFalse(result)

