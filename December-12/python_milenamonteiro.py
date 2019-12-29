import json
from math import pow, sin, cos, sqrt, atan2, pi, degrees

def json_distance(coordinates):
    markers = json.loads(coordinates)
    start = markers['markers'][0]['location']
    end = markers['markers'][1]['location']
        
    degree_to_rad = float(pi / 180.0)
    d_lat = (end[0] - start[0]) * degree_to_rad
    d_long = (end[1] - start[1]) * degree_to_rad
    
    # distance
    a = pow(sin(d_lat/2),2) + cos(start[0]*degree_to_rad) * cos(end[0]*degree_to_rad) * pow(sin(d_long/2),2)
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    d = 6367 * c
    
    # direction
    y = sin(d_long) * cos(end[0])
    x = cos(start[0]) * sin(end[0]) - sin(start[0]) * cos(end[0]) * cos(d_long)
    brng = degrees(atan2(y, x))
    
    bearings = ["NE", "E", "SE", "S", "SW", "W", "NW", "N"]

    index = brng - 22.5
    if (index < 0): index += 360;
    index = int(index / 45)

    directions = json.dumps(
        {
            "directions":
                [
                    {
                        "message": "Go get'em",
 	                    "distance": round(d, 2),
 	                    "direction": bearings[index]
 	                }
                ]
        }
    , indent=2)
    
    return directions

print(json_distance('{"markers": [{"name": "start","location": [25.1212, 55.1535]},{"name": "destination","location": [25.2285, 55.3273]} ]}'))
