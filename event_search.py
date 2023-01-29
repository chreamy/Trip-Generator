import ticketpy
import constants
import event_images
tm_client = ticketpy.ApiClient('45LwqqL0VU4G5PGAIsAnYebkwpNRQpGf')

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
    out = []
    for page in pages:
        for event in page:
            out+=event_images.screenshot(event.name)
    print(out[:3])
    return out[:3]
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
    return search(cities[index],subject,start_date,end_date)

# Example
#search("Atlanta",'sports','2023-02-15T00:00:00Z','2023-02-20T00:00:00Z')


