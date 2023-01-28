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

"""

from radius import radius
import pprint
from exscraper import ticket
import json
codes = {'ATL','LAX','ORD'}
#codes = {'ATL','LAX','ORD','DFW','DEN','JFK','SFO','SEA','MCO','LAS','CLT','EWR','PHX','IAH','MIA','BOS','MSP','DTW','PHL','BWI','SLC','SAN','IAD','DCA','TPA','MDW'}
miles = 25
milestometers = 1609.34
rad = miles* milestometers
#initial input
type = 'war_memorials'
loc = 'IAH'
date = '2023-02-25'

max = []
apt,placeslist = '',[]
for code in codes:
    try:
        count, places = radius(code,type,rad)
    except:
        print(code,'invalid')
        count = -1
    print(code,'has',count,type,'in',miles,'miles')
    max.append({'name': code, 'count':count, 'placeslist' : places})
max = sorted(max, key=lambda x: x['count'],reverse = True)
outfile = open(f'{max[0]["name"]}_{max[1]["name"]}_{max[2]["name"]}_{type}.json', "w")
out = []
for i in range(3):
    print(f'option{i} {max[i]["name"]} {type}')
    max[i]['placeslist'] = sorted(max[i]['placeslist'], key=lambda x: x['properties']['rate'], reverse=True)
    out.append({'city':max[i]["name"],'places':[{'name':place['properties']['name'],'lon':place['geometry']['coordinates'][0],'lat':place['geometry']['coordinates'][1],'dist':place['properties']['dist']} for place in max[i]['placeslist'][:10]]})
    ticket(loc,max[i]["name"],date)
json.dump(out, outfile, sort_keys=True, indent=4)
outfile.close()
