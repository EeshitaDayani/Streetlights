import pandas as pd
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="extract_coordinates")
location = geolocator.geocode("University of Waterloo")
print(location.address)
print((location.latitude, location.longitude))
