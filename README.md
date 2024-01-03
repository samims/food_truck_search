# Food Truck Search
API for searching food truck on San Francisco within 5 km of range

## Features
- seed the data using management command
- single command for running the project
- postgis for spatial and distance calculation
- validation of lat lang, roughly makes this project usable for San Francisco
- easily configurable boundary from django settings

## How to run
Copy the env.local and create .env with save values
and run

```shell
docker-compose up --build
```

Then open the `food_truck_web_shell` using 
```shell
docker exec -it food_truck_web /bin/bash
```
To seed the DB from `CSV` file run 
```python
python manage.py load
```
this will run a management command and seed the DB

To Run the test run this in same shell
```python
python manage.py test
```


## Usage of API
When the project is running you can access the Search api which accepts few query params

| Parameter | Type   | Required      |
|-----------|--------|---------------|
| lat       | float  | Yes           |
| long      | float  | Yes           |
| radius    | int    | No(default 5) |
| limit     | int    | Yes           |
| offset    | int    | Yes           |

Example usage:
```curl
curl "http://127.0.0.1:3000/search?lat=37.67751326467553&limit=5&long=-122.3970441344819&offset=1&radius=5"
```

# Difficulties I faced
Though it shouldn't be written in README but as asked on requirement I am mentioning
few
1. New topic to me, as I never used PostGIS before, though heard about it 
2. Was getting issue from gdal as the solution provided over internet was not working. Ubuntu removed the repo though
   from official repository as per my research
3. Requirement was vague so had to take liberties to assume few things(which is dangerous generally)

## Future improvements
Few things could be implemented, if there was time or enough requirements
- filter based on status
- filter based on opening time
- filter based on radius(suppose the food truck is within the radius but not in San Francisco)
- done more R&D about lat lang
- write more and effective test cases
- deploy to some free tier PAAS
- etc...


## Acknowledgements
I used the docker image I am providing the link below which has already installed postgis 
extension. Which was helpful rather than creating on my own during this time
https://github.com/kartoza/docker-postgis
