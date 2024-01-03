from django.conf import settings


def is_in_valid_lat_long(lat: float, long: float) -> bool:
    """
    Checks if the provided latitude and longitude fall within a valid range.

    Args:
        lat (float): Latitude to validate.
        long (float): Longitude to validate.

    Returns:
        bool: True if the latitude and longitude are within valid boundaries, False otherwise.
    """
    min_lat = settings.MIN_LAT
    max_lat = settings.MAX_LAT
    min_long = settings.MIN_LONG
    max_long = settings.MAX_LONG
    # should be in the range of min_lat and max_lat
    is_valid_lat = min_lat <= lat <= max_lat
    # should be in the range of min_long, max_long
    is_valid_long = min_long <= long <= max_long

    return is_valid_lat and is_valid_long


