import requests
import json
from airportfinder import airportinfo
import airport_database
def radius(airport,type,rad):
    try:
        log,lat,city = airportinfo(airport)
    except:
        print('no result')
        return
    url = f'https://api.opentripmap.com/0.1/en/places/radius?radius={rad}&lon={log}&lat={lat}&kinds={type}&apikey=5ae2e3f221c38a28845f05b6582feb78b4109c243d59513273d90e00'
    response = requests.get(url)
    #print(url)
    #print(response.status_code,response.text)
    #print(len(json.loads(response.text)['features']),'results found within',rad,'meters')
    """outfile = open(f"{type} within {rad} meters radius of {airport}.json", "w")
    json.dump(json.loads(response.text), outfile, sort_keys=True, indent=4)
    outfile.close()"""
    return len(json.loads(response.text)['features']),json.loads(response.text)['features'],city
#radius('IAH','amusement_parks',400000)