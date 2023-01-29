from airport import airport


def load_airport_database():
    database = {}

    with open('airport_database.txt') as file:
        data = file.read().splitlines()
        for line in data:
            line = line.split(':')
            database.update({line[1]: airport(IATA=line[1],
                                              name=line[2],
                                              city=line[3],
                                              lat=line[14],
                                              long=line[15])})

    return database


db = load_airport_database()


def city(IATA):
    return db.get(IATA).city


def name(IATA):
    return db.get(IATA).name



def lat(IATA):
    return float(db.get(IATA).lat)


def long(IATA):
    return float(db.get(IATA).long)

