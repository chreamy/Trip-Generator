
## Description

Usage of a multitude of APIs, machine learning, data science, and online marketing campaigns to delever personalized flights for users.

## Event 

>*module **event_search***

The module *event_search* provides function *optimal()* to return the city with the highest frequency of the specified event.


>*module **event_images***

The module *event_images* provides function *screenshot()* to return a source file of screenshot image.


## Flight Data 

>*class **airport**(IATA, name, city, lat, long)

The class *airport* onsists of the following class variables: IATA (International Air Transport Association) , name of the airport, city, latitude, and longitude of the airport. These variables will be initialized during class intialization. This class is used in *load_airport_database()*, where the function parses and returns a dictionary mapping each IATA to an *airport* object.


>*class **flight**(price)*

The class *flight* consists of the following class variables: price and path. Price is initialized at class initialization. Path is set to an empty list. The class provides a *add_path(short_path)* function that appends a *short_path* object to the list. This structure is used to account for multiple flights (transfer flights) until reaching final destination.


>*class **short_path**(dep_IATA, arr_IATA, dep_terminal, arr_terminal, dep_time, arr_time, time, aircraft, carrier)

The classs *short_path* stores variables for the details a singular flight including deperature time and arrival time. 


>*class **attraction**(city, lat, long)

The class *attraction* consists of the following class variable, initialized at class initialization: city, latititude, and longitude of the airport. 


>*class **interactive_map**()*

The class *interactive_map* provides a function *create_map()* that creates an interactive map with markers marked at sepecific coordinates (for each airport location) and flight route connecting the coordinates. 


>*module **bestairport***

The module *bestairport* returns a list of IATA locations based on event density.


> *module **flight_ticket

The module *flight_ticket* provides function *screenshot()* with parameters: IATA at departure, IATA at destination, and date. The function returns a generated image of the flight ticket. based on the provided arguments.


## Email

>*class **HackathonEmails**()*

The class cretes a function that callls 


>*module **EmailAiGen*** 

The module EmailAiGen processes, collect, and outputs data.


>*module **textgen***

The module *textgen* accesses word generation processing API to build message for output.


## Quick Installations

Several python modules were used for this application. 

**Installation**

```
$ pip install folium
```

The *folium* module allows the user to visualize data by creating an interactive leaflet map in a separate HTML file. 


```
$ pip install selenium
```

The *selenium* module is designed for automation. In this instance, the module is used to create screenshots of *png* screenshots.






