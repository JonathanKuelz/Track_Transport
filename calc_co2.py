#from process_kml import process
from pandas import Series

#emissions per km per person for different means of transport
co2_transport = {
    'On a train': 14,
    'Driving': 100,
    'Running': 0,
    'Moving': 0,
    'Walking': 0,
    'Plane': 285,
    'On the subway': 14,
    'On a bus': 68,
    'On a tram': 23
}

def counter_day(dict_day):
    emission = {}
    emission['Date'] = dict_day['Date']
    transport_means = Series(dict_day['Transport'])
    co2permean = transport_means.map(co2_transport)
    kms = list(map(int, dict_day['Distance']))
    #print(kms)
    #print(co2permean)
    emission['co2_emission'] = sum([a*b for a,b in zip(co2permean, kms)])
    return emission


def counter_timeline(timeline):
    timeline_emissions = []
    for index in range(len(timeline)):
        timeline_emissions.append(counter_day(timeline[index]))
    return timeline_emissions