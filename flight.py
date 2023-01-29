class flight:
    def __init__(self, price):
        self.price = price
        self.path = []

    def add_path(self, short_path):
        self.path.append(short_path)


class short_path:
    def __init__(self, dep_IATA,
                 arr_IATA,
                 dep_terminal,
                 arr_terminal,
                 dep_time,
                 arr_time,
                 time,
                 aircraft,
                 carrier):
        self.dep_IATA = dep_IATA
        self.arr_IATA = arr_IATA
        self.dep_terminal = dep_terminal
        self.arr_terminal = arr_terminal
        self.dep_time = dep_time
        self.arr_time = arr_time
        self.time = time
        self.aircraft = aircraft
        self.carrier = carrier
