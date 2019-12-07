#from process_kml import process
from pandas import Series

#emissions in kg per km per person for different means of transport
co2_transport = {
    'On a train': 0.014,
    'Driving': 0.100,
    'Running': 0.0,
    'Moving': 0.0,
    'Walking': 0.0,
    'Plane': 0.285,
    'On the subway': 0.014,
    'On a bus': 0.068,
    'On a tram': 0.023
}


def counter_day(dict_day):
    emission = {}
    emission['Date'] = dict_day['Date']
    transport_means = Series(dict_day['Transport'])
    co2permean = transport_means.map(co2_transport)
    ms = list(map(int, dict_day['Distance']))
    kms = [x / 1000 for x in ms]
    #print(kms)
    #print(co2permean)
    emission['co2_emission'] = sum([a*b for a,b in zip(co2permean, kms)])
    return emission


def counter_timeline(timeline):
    timeline_emissions = []
    for index in range(len(timeline)):
        timeline_emissions.append(counter_day(timeline[index]))
    return timeline_emissions
