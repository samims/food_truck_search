from django.test import TestCase
from django.contrib.gis.geos import Point
from model_bakery import baker

from food_truck.models import FoodTruck
from food_truck.selector import FoodTruckRepository


class FoodTruckRepositoryTestCase(TestCase):
    def setUp(self):
        # Set up food trucks with specific locations
        self.food_truck1 = baker.make(FoodTruck,
                                      applicant="Truck1",
                                      latitude=37.75008693198698,
                                      longitude=-122.40880648110114,
                                      )
        #     FoodTruck.objects.create(
        #     applicant="Truck1",
        #     location=Point(-122.41880648110114, 37.76008693198698, srid=4326),
        #     location_id=122.418806,
        # )
        # This truck should be the closest to the test coordinates
        self.food_truck2 = baker.make(FoodTruck,
                                      applicant="Truck2",
                                      latitude=37.77008693198698,
                                      longitude=-122.43882648110114
                                      )
        # FoodTruck.objects.create(
        #     applicant="Truck2",
        #     location=Point(-122.41882648110114, 37.76008693198698, srid=4326)
        # )
        # FoodTruck.objects.create(
        #     applicant="Truck3",
        #     location=Point(-122.42880648110114, 37.75008693198698, srid=4326)
        # )

    def test_get_food_truck_by_lat_long_and_radius(self):
        # Test coordinates that are closest to 'Truck2'
        lat = 37.76008693198698
        long = -122.42880648110114
        radius = 1  # Your specified radius

        # Fetch food trucks within the specified radius
        result = FoodTruckRepository.get_food_truck_by_lat_lang_and_radius(lat, long, radius)

        # Assert that the closest truck matches the expected result ('Truck2')
        self.assertEqual(result[0].applicant, "Truck2")
