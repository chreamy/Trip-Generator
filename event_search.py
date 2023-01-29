import ticketpy
import constants

tm_client = ticketpy.ApiClient(constants.ticketmaster_key)

def search(city,subject,start_date,end_date):
    '''

    :param cities: An array of cities
    :param subject: An event subjects
    :param start_date: Starting date to search events
    :param end_date: End date to search events
    :return: A printout of all of the located events
    '''
    pages = tm_client.events.find(
        classification_name=f'{subject}',
        city=f'{city}',
        start_date_time=start_date,
        end_date_time=end_date
    )
    for page in pages:
        for event in page:
            print(event)
def optimal(cities,subject,start_date,end_date):
    '''

    :param cities: An array of cities
    :param subject: An event subjects
    :param start_date: Starting date to search events
    :param end_date: End date to search events
    :return: City with the highest frequency of the specified event
    '''
    frequencies = []
    for c in cities:
        pages = tm_client.events.find(
            classification_name=f'{subject}',
            city=f'{c}',
            start_date_time=start_date,
            end_date_time=end_date
        )
        count = 0
        for page in pages:
            for event in page:
                count += 1
        frequencies += [count]
    print(frequencies)
    max_val = max(frequencies)

    index = frequencies.index(max_val)
    return cities[index]

# Example
cities = ['Atlanta', 'Houston', 'New York','Los Angeles']
print(optimal(cities,'sports','2023-02-15T00:00:00Z','2023-02-20T00:00:00Z'))


