import json
from flight import flight, short_path


def load_flight_routes():
    with open('data.json') as file:
        data = json.load(file)
        # list of flight routes
        flight_routes = []
        for f in data.get('tickets'):
            flight_ = flight(price=f.get('price'))
            for p in f.get('itineraries'):
                short_path_ = short_path(dep_IATA=p.get('depart')[0],
                                        arr_IATA=p.get('arrive')[0],
                                        dep_terminal=p.get('depart')[1],
                                        arr_terminal=p.get('arrive')[1],
                                        dep_time=p.get('depart')[2],
                                        arr_time=p.get('arrive')[2],
                                        time=p.get('duration'),
                                        aircraft=p.get('aircraft'),
                                        carrier=p.get('carrier'))
                flight_.add_path(short_path_)
            flight_routes.append(flight_)

    return flight_routes



