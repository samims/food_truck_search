import json
import logging

from datetime import datetime
from typing import Union

from django.contrib.gis.geos import Point
from django.utils.timezone import make_aware

from food_truck.models import FoodTruck

logger = logging.getLogger(__name__)


def read_data():
    """
    Reads data from the provided csv file
    only issue is it's in json format so need to do accordingly
    """
    file_name = "food-truck-data.csv"

    with open(file_name, 'r') as csv_file:
        content = csv_file.read()

    formatted_content = content.replace('\n', '').replace('payload:', '"payload":').replace('fileTree:', '"fileTree":')

    # Convert the reformatted content to a Python dictionary
    data_dict = json.loads(formatted_content)

    file_items = data_dict['payload']['blob']['csv']

    # first line contains column names, so just cut the crap :-)
    rows = file_items[1:]

    for row in rows:
        # approved 19 date time
        # expiration_date 22 date time
        # PriorPermit 21 change to boolean

        approved_date = row[19]
        expiration_date = row[22]
        prior_permit = row[21]

        formatted_approved_date = format_date_for_model(approved_date)
        formatted_expiration_date = format_date_for_model(expiration_date)
        formatted_prior_permit = bool(int(prior_permit))
        location = Point(float(row[14]), float(row[15]))

        food_truck = FoodTruck.objects.create(
            location_id=row[0],
            applicant=row[1],
            facility_type=row[2],
            cnn=row[3],
            location_description=row[4],
            address=row[5],
            block_lot=row[6],
            block=row[7],
            lot=row[8],
            permit=row[9],
            status=row[10],
            food_items=row[11],
            x=row[12],
            y=row[13],
            latitude=row[14],
            longitude=row[15],
            location=location,
            schedule=row[16],
            days_hours=row[17],
            noi_sent=row[18],
            approved=formatted_approved_date,
            received=row[20],
            prior_permit=formatted_prior_permit,
            expiration_date=formatted_expiration_date,
            fire_prevention_district=row[24],
            police_district=row[25],
            supervisor_district=row[26],
            zip_code=row[27],
            neighbourhoods=row[28]
        )

        logger.info(f"food truck saved with id {food_truck.id, food_truck}")


def format_date_for_model(date_str: Union[str, None]) -> Union[str, None]:
    """
    Converts a date string to a timezone-aware datetime object.

    Args:
    - date_str (Union[str, None]): A string representing a date in the format '%m/%d/%Y %I:%M:%S %p'.

    Returns:
    - Union[str, None]: A string representation of the formatted date or None if input is invalid.

    This function converts the given date string to a timezone-aware datetime object
    using the format '%m/%d/%Y %I:%M:%S %p'. If the input string is not in the expected format,
    it logs a warning and returns None.
    """
    formatted_date = None
    if date_str:
        try:
            python_datetime = datetime.strptime(date_str.strip(), '%m/%d/%Y %I:%M:%S %p')
            formatted_date = make_aware(python_datetime)
        except ValueError as e:
            logger.warning(f"Error formatting date {date_str}: {e}")
    return formatted_date
