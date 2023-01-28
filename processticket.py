import pprint
import json

def process(rawdat):
    x = [rawdat][0]
    data = x['data']
    dict = x['dictionaries']
    out = []
    for ticket in data:
        obj = {'id':ticket['id'],'segments':len(ticket['itineraries'][0]['segments']),'itineraries':[],'price':ticket['price']['total']}
        for i in ticket['itineraries'][0]['segments']:
           obj['itineraries'].append({
               'duration':i['duration'][2:],
               'aircraft':dict['aircraft'][i['aircraft']['code']],
               'carrier': dict['carriers'][i['carrierCode']],
               'depart':[
                   i['departure']['iataCode'],
                   i['departure']['terminal'],
                   i['departure']['at']
               ],
               'arrive':[
                   i['arrival']['iataCode'],
                   i['arrival']['terminal'],
                   i['arrival']['at']]
           })
        out.append(obj)
    return out