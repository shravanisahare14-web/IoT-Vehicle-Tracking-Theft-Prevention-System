import json
import time
import random
import os
from math import radians, sin, cos, sqrt, atan2

DATA_FOLDER = "data"
LOCATION_FILE = os.path.join(DATA_FOLDER, "latest_location.json")
ANALYTICS_FILE = os.path.join(DATA_FOLDER, "analytics.json")

os.makedirs(DATA_FOLDER, exist_ok=True)

route = [
    (17.3850, 78.4867),
    (17.3852, 78.4869),
    (17.3854, 78.4871),
    (17.3857, 78.4875),
    (17.3860, 78.4880),
    (17.3865, 78.4885),
    (17.3868, 78.4889),
    (17.3872, 78.4893),
    (17.3875, 78.4897),
    (17.3879, 78.4902)
]

CENTER_LAT = 17.3850
CENTER_LON = 78.4867
GEOFENCE_RADIUS = 250

speed_history = []
threat_history = []

total_distance = 0
threat_events = 0
breaches = 0

index_pos = 0
previous_lat = None
previous_lon = None


def calculate_distance(lat1, lon1, lat2, lon2):
    r = 6371000

    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)

    a = (
        sin(dlat / 2) ** 2
        + cos(radians(lat1))
        * cos(radians(lat2))
        * sin(dlon / 2) ** 2
    )

    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return r * c


print("GuardianTrack Simulator Started")
print("--------------------------------")

while True:

    lat, lon = route[index_pos]

    speed = random.randint(20, 80)

    distance_from_center = calculate_distance(
        CENTER_LAT,
        CENTER_LON,
        lat,
        lon
    )

    geofence = (
        "SAFE"
        if distance_from_center <= GEOFENCE_RADIUS
        else "BREACHED"
    )

    threat = (
        "SAFE"
        if geofence == "SAFE"
        else "ALERT"
    )

    if previous_lat is not None:

        travelled = calculate_distance(
            previous_lat,
            previous_lon,
            lat,
            lon
        )

        total_distance += travelled / 1000

    previous_lat = lat
    previous_lon = lon

    if threat == "ALERT":
        threat_events += 1
        breaches += 1

    speed_history.append(speed)
    threat_history.append(
        1 if threat == "ALERT" else 0
    )

    speed_history = speed_history[-20:]
    threat_history = threat_history[-20:]

    average_speed = (
        round(
            sum(speed_history)
            / len(speed_history),
            2
        )
        if speed_history
        else 0
    )

    location_data = {
        "lat": lat,
        "lon": lon,
        "speed": speed,
        "engine": "ON",
        "threat": threat,
        "geofence": geofence,
        "distance_from_center":
            round(distance_from_center, 2)
    }

    analytics_data = {
        "total_distance":
            round(total_distance, 3),

        "average_speed":
            average_speed,

        "breaches":
            breaches,

        "threat_events":
            threat_events,

        "speed_history":
            speed_history,

        "threat_history":
            threat_history
    }

    with open(
        LOCATION_FILE,
        "w"
    ) as file:

        json.dump(
            location_data,
            file,
            indent=4
        )

    with open(
        ANALYTICS_FILE,
        "w"
    ) as file:

        json.dump(
            analytics_data,
            file,
            indent=4
        )

    print(location_data)

    index_pos += 1

    if index_pos >= len(route):
        index_pos = 0

    time.sleep(3)