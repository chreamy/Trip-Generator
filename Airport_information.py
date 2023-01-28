class airport_information:
    def __init__(self, name, city, lat, long):
        self.name = name
        self.city = city
        self.lat = lat
        self.long = long

    def __str__(self):
        s = ''
        s += 'Name: ' + self.name + '\n'
        s += 'city: ' + self.city + '\n'
        s += 'coordinates: ' + self.lat + ', ' + self.long + '\n'
        return s
