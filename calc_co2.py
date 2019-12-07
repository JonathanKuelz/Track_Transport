#from process_kml import process


#emissions per km per person for different means of transport
co2_transport = {
    'Train': 14,
    'Car': 100,
    'Running': 0,
    'Walking': 0,
    'Plane': 285,
    'On the subway': 14,
    'On a bus': 68
}


def counter_day(dict_day):
    emission = {}
    emission['Date'] = dict_day['Date']
    transport_means = Series(dict_day['Transport'])
    co2permean = transport_means.map(co2_transport)
    emission['co2_emission'] = sum([a*b for a,b in zip(co2permean, dict_day['Distance'])])
    return emission


def counter_timeline(timeline):
    timeline_emissions = []
    for index in range(len(timeline)):
        timeline_emissions.append(counter_day(timeline[index]))
    return timeline_emissions
