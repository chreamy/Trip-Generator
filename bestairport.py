"""
things to consider:
1. more than one offer
2. best radius default val make into function
3. location & ticket preferences?
4. see if direct flight available before checking density
5. sort locations and search descriptions using wikidata id
6. download images from site name and include in html
7. exclude duplicate sites?
8. convert keywords into location keywords
9. onlt AA airplanes?

"""

from radius import radius
import pprint
from exscraper import ticket
import json
def getplaces(miles,type,loc,date):
    keyword = type.replace(" ", "_").lower()
    codes = {'ATL','LAX','ORD','DFW','DEN'}
    #codes = {'ATL','LAX','ORD','DFW','DEN','JFK','SFO','SEA','MCO','LAS','CLT','EWR','PHX','IAH','MIA','BOS','MSP','DTW','PHL','BWI','SLC','SAN','IAD','DCA','TPA','MDW'}
    milestometers = 1609.34
    rad = miles* milestometers
        #initial input

    max = []
    apt,placeslist = '',[]
    for code in codes:
        try:
            count, places, city = radius(code,keyword,rad)
        except:
            print(code,'invalid')
            count = -1
            places = []
        print(code,'has',count,type,'in',miles,'miles')
        max.append({'name': code, 'city':city, 'count':count, 'placeslist' : places})
    max = sorted(max, key=lambda x: x['count'],reverse = True)
    #outfile = open(f'{max[0]["name"]}_{max[1]["name"]}_{max[2]["name"]}_{type}.json', "w")
    out = []

    print(f'best is {max[0]["name"]}')
    max[0]['placeslist'] = sorted(max[0]['placeslist'], key=lambda x: x['properties']['rate'], reverse=True)
    out={'code':max[0]["name"], 'city':max[0]['city'],'tickets':ticket(loc,max[0]["name"],date),'places':[{'name':place['properties']['name'],'lon':place['geometry']['coordinates'][0],'lat':place['geometry']['coordinates'][1],'dist':place['properties']['dist']} for place in max[0]['placeslist'][:10]]}
    #json.dump(out, outfile, sort_keys=True,indent=4)
    #outfile.close()
    return out