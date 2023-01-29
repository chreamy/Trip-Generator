import ticketpy
import constants

tm_client = ticketpy.ApiClient(constants.ticketmaster_key)

pages = tm_client.events.find(
    classification_name='sports',
    city='Atlanta',
    start_date_time='2023-02-15T20:00:00Z',
    end_date_time='2023-02-20T20:00:00Z'
)

for page in pages:
    for event in page:
        print(event)