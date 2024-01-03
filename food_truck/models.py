from django.db import models
from django.contrib.gis.db import models as gis_models
from django.contrib.gis.geos import Point
from core.models import BaseModel

# facility choices for db & representation options
PUSH_CART = 'P'
TRUCK = 'T'

FACILITIES = (
    (PUSH_CART, "Push Cart"),
    (TRUCK, "Truck"),
)

EXPIRED = 'EXP'
APPROVED = 'APV'
REQUESTED = "REQ"
ISSUED = "ISD"
SUSPEND = "SPD"

STATUS_CHOICES = (
    (EXPIRED, "Expired"),
    (APPROVED, "Approved"),
    (REQUESTED, "Requested"),
    (ISSUED, "Issued"),
    (SUSPEND, "Suspend")
)


class FoodTruck(BaseModel):
    """
    Holds the info related to food truck
    this is the only model/table we will be using for now
    """
    location_id = models.BigIntegerField(db_index=True, unique=True)
    applicant = models.CharField(blank=False, max_length=255, help_text="name of the truck/restaurant")
    facility_type = models.CharField(choices=FACILITIES, null=True,
                                     max_length=30, db_index=True,
                                     help_text="if it's truck, push cart etc.")
    cnn = models.BigIntegerField()
    location_description = models.TextField(null=True)
    address = models.TextField()
    block_lot = models.CharField(max_length=10, null=True)
    block = models.CharField(max_length=10, null=True)
    lot = models.CharField(max_length=10, null=True)
    permit = models.CharField(max_length=30)
    status = models.CharField(choices=STATUS_CHOICES, max_length=20, db_index=True)
    food_items = models.TextField(null=True)
    x = models.CharField(max_length=20, null=True)
    y = models.CharField(max_length=20, null=True)

    # will be used for search
    latitude = gis_models.DecimalField(max_digits=40, decimal_places=20, db_index=True)
    longitude = gis_models.DecimalField(max_digits=40, decimal_places=20)
    location = gis_models.PointField(db_index=True, null=True)

    schedule = models.URLField()
    days_hours = models.CharField(max_length=60, null=True)
    noi_sent = models.CharField(max_length=10, null=True)
    approved = models.DateTimeField(null=True)
    received = models.BigIntegerField()
    prior_permit = models.BooleanField(db_index=True)
    # TODO: more than expiration date it will be expired check if null
    expiration_date = models.DateTimeField(null=True)
    fire_prevention_district = models.CharField(max_length=5, null=True)
    police_district = models.CharField(max_length=10, null=True)
    supervisor_district = models.CharField(max_length=10, null=True)
    # will be used in response
    zip_code = models.CharField(max_length=10, null=True)
    neighbourhoods = models.CharField(max_length=255, null=True)

    def save(self, *args, **kwargs):
        if self.latitude is not None and self.longitude is not None and self.location is None:
            self.location = Point(self.longitude, self.latitude)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.applicant
