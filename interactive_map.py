import folium
import flight_information
import attraction_information
import airport_database
from selenium import webdriver
import os
import time
import upload


def create_map(data):
    flight_routes = flight_information.load_flight_routes(data)
    start = flight_routes[0].path[0].dep_IATA
    start_coordinates = airport_database.lat(start), airport_database.long(start)

    end = flight_routes[0].path[-1].arr_IATA
    end_coordinates = airport_database.lat(end), airport_database.long(end)

    # specific cases
    print(start_coordinates[1])
    print(end_coordinates[1])
    long_difference = start_coordinates[1] - end_coordinates[1]

    if long_difference > 0:
        start_icon = 'icons/start2.png'
        end_icon = 'icons/end2.png'
    else:
        start_icon = 'icons/start.png'
        end_icon = 'icons/end.png'

    airport_tooltip = 'Click For Airport Details'

    f = folium.Figure(width=100, height=50)
    m = folium.Map(location=[(end_coordinates[0]+start_coordinates[0])/2,(end_coordinates[1]+start_coordinates[1])/2],
                   zoom_start=4,
                   min_zoom=4,
                   max_zoom=16).add_to(f)

    icon = folium.features.CustomIcon(start_icon, icon_size=(20, 20))
    folium.Marker(location=[airport_database.lat(start), airport_database.long(start)],
                  popup='<b>' + airport_database.city(start) + '</b><BR>' + airport_database.name(start),
                  tooltip=airport_tooltip,
                  icon=icon).add_to(m)

    attractions = attraction_information.load_attractions()
    attraction_tooltip = 'Click for Attraction Details'

    for a in attractions:
        icon = folium.features.CustomIcon('icons/attraction.png', icon_size=(5, 5))
        folium.Marker(location=[round(a.lat, 3), round(a.long, 3)],
                      popup='<b>' + a.name + '</b>',
                      tooltip=attraction_tooltip,
                      icon=icon).add_to(m)

    for flight in flight_routes:
        list_IATA = []
        for short_path in flight.path:
            if short_path.dep_IATA not in list_IATA:
                list_IATA.append(short_path.dep_IATA)
            if short_path.arr_IATA not in list_IATA:
                list_IATA.append(short_path.arr_IATA)

        list_coordinates = []
        for IATA in list_IATA:
            list_coordinates.append([airport_database.lat(IATA), airport_database.long(IATA)])
            if IATA == list_IATA[0]:
                continue

            icon = folium.features.CustomIcon('icons/mid.png', icon_size=(15, 15))
            if IATA == list_IATA[-1]:
                icon = folium.features.CustomIcon(end_icon, icon_size=(20, 20))

            folium.Marker(location=[airport_database.lat(IATA), airport_database.long(IATA)],
                          popup='<b>' + airport_database.city(IATA) + '</b><BR>' + airport_database.name(IATA),
                          tooltip=airport_tooltip,
                          icon=icon).add_to(m)

        folium.PolyLine(list_coordinates,
                        weight=1.5,
                        dash_array='3').add_to(m)

    mapUrl = 'file://{0}/{1}'.format(os.getcwd(), 'map.html')
    driver = webdriver.Chrome()
    m.save('map.html')
    driver.get(mapUrl)
    time.sleep(5)
    driver.save_screenshot('map.png')
    driver.quit()


    return upload.upload('./map.png')


#create_map()
def create_attraction_map(data):
    flight_routes = flight_information.load_flight_routes(data)
    start = flight_routes[0].path[0].dep_IATA
    start_coordinates = airport_database.lat(start), airport_database.long(start)

    end = flight_routes[0].path[-1].arr_IATA
    end_coordinates = airport_database.lat(end), airport_database.long(end)
    global y
    f = folium.Figure(width=100, height=50)
    m = folium.Map(location=[end_coordinates[0], end_coordinates[1]],
                   zoom_start=11,
                   min_zoom=4,
                   max_zoom=24).add_to(f)

    attractions = attraction_information.load_attractions()

    for a in attractions:



        icon = folium.features.CustomIcon('icons/attraction.png', icon_size=(30, 30))
        folium.Marker(location=[round(a.lat, 3), round(a.long, 3)],
                      popup=folium.Popup("<b>" + a.name + "</b>"),
                      icon=icon).add_to(m)


    mapUrl = 'file://{0}/{1}'.format(os.getcwd(), 'map2.html')
    driver = webdriver.Chrome()
    m.save('map2.html')
    driver.get(mapUrl)
    time.sleep(5)
    driver.save_screenshot('map2.png')
    driver.quit()
    return upload.upload('./map2.png')



