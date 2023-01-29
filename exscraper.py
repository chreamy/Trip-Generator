import requests
import json
import processticket
def ticket(org,des,date):
    print(org,des,date)
    consumer_key = "FKkkVIgmjbAZDhRKIdgEyBb3cd9XaI3R"
    consumer_secret = "AzWpPCrnJP3Jgfgk"
    payload = {
    'grant_type': 'client_credentials',
    'client_id': consumer_key,
    'client_secret': consumer_secret
    }
    dat = {"currencyCode": "USD",
           "originDestinations": [
    {
      "id": "1",
      "originLocationCode": org,
      "destinationLocationCode": des,
      "departureDateTimeRange": {
        "date": date
      }
    }
  ],
  "travelers": [
    {
      "id": "1",
      "travelerType": "ADULT"
    }
  ],
  "sources": [
    "GDS"
  ],
  "searchCriteria": {
    "maxFlightOffers": 5,
    "flightFilters": {
      "cabinRestrictions": [
        {
          "cabin": "ECONOMY",
          "coverage": "MOST_SEGMENTS",
          "originDestinationIds": [
            "1"
          ]
        }
      ]
    }
  }
}
    r = requests.post("https://test.api.amadeus.com/v1/security/oauth2/token",
                  headers={"Content-Type": "application/x-www-form-urlencoded"},
                  data=payload)
    rlist = json.loads(r.text)
    #print(r.status_code,r.text)
    #print(rlist['access_token'])
    response = requests.post('https://test.api.amadeus.com/v2/shopping/flight-offers', headers={'Authorization': str('Bearer '+rlist['access_token'])},json = dat)
    #print(response.status_code,response.text)
    #outfile = open(f"{org}_{des}_{date}.json", "w")
    #json.dump(processticket.process(json.loads(response.text)), outfile, sort_keys=True, indent=4)
    #json.dump(json.loads(response.text), outfile, sort_keys=True, indent=4)
    #outfile.close()
    return processticket.process(json.loads(response.text))
#ticket('JFK','EWR','2023-02-15')