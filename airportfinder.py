import requests
import json
import Airport_database
def airportinfo(code):
    consumer_key = "FKkkVIgmjbAZDhRKIdgEyBb3cd9XaI3R"
    consumer_secret = "AzWpPCrnJP3Jgfgk"
    payload = {
    'grant_type': 'client_credentials',
    'client_id': consumer_key,
    'client_secret': consumer_secret
    }
    r = requests.post("https://test.api.amadeus.com/v1/security/oauth2/token",
                  headers={"Content-Type": "application/x-www-form-urlencoded"},
                  data=payload)
    rlist = json.loads(r.text)
    if r.status_code!=200:
        print('invalid input')
        return
    response = requests.get(f'https://test.api.amadeus.com/v1/reference-data/locations?subType=AIRPORT&keyword={code}', headers={'Authorization': str('Bearer '+rlist['access_token'])})
    if json.loads(response.text)['meta']['count']==0:
        print('no result')
        return
    """outfile = open(f"airport {code}.json", "w")
    json.dump(json.loads(response.text), outfile, sort_keys=True, indent=4)
    outfile.close()"""
    db = Airport_database.import_database()
    long = db.get(code).long
    lat = db.get(code).lat
    #long = (json.loads(response.text)['data'][0]['geoCode']['longitude'])
    #lat = (json.loads(response.text)['data'][0]['geoCode']['latitude'])
    return long,lat