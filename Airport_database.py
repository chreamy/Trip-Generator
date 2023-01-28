from Airport_information import airport_information


def import_database():
    database = {}
    IATA_codes = set()

    with open('Airport_database.txt') as file:
        data = file.read().splitlines()
        for line in data:
            line = line.split(':')
            IATA_codes.add(line[1])
            database.update({line[1]: airport_information(name=line[2],
                                                          city=line[3],
                                                          lat=line[14],
                                                          long=line[15])})
    return database