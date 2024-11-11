import math
from geopy.distance import geodesic

def calculate(p1, p2):
    R = 6371  # Radius of the Earth in km
    lat1, lon1 = p1
    lat2, lon2 = p2
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = R * c
    return distance

def calculate_distance(coord1, coord2):
    return geodesic((coord1['lat'], coord1['lon']), (coord2['lat'], coord2['lon'])).kilometers