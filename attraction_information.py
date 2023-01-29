import json
from attraction import attraction

def load_attractions():
    with open('data.json') as file:
        data = json.load(file)
        # list of attractions
        attractions = []
        for place in data.get('places'):
            attractions.append(attraction(name=place.get('name'),
                                          lat=place.get('lat'),
                                          long=place.get('lon')))

    return attractions


