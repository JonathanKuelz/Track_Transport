import re

from pykml import parser as kml_parser
from lxml import etree


def read_kml(filepath):
    with open(filepath, 'rt', encoding='utf-8') as kml:
        track_kml = kml_parser.parse(kml)

    track = etree.tostring(track_kml, pretty_print=False)
    return str(track)


def process_trackstring(track):
    matches = {'Date': '', 'Transport': [], 'Distance': []}
    regex_dict = {
        'Date': re.compile('(?<=Location history from )([0-9]{4}-[0-9]{2}-[0-9]{2})(?= to [0-9]{4}-[0-9]{2}-[0-9]{2})'),
        'Transport': re.compile('(?<=\"Category\"><value>)'
                                '(Running|Walking|On the subway|On a bus|Moving|Driving|On a tram|On a train)(?=<)'),
        'Distance': re.compile('(?<=[a-zA-Z]</value></Data><Data name=\"Distance\"><value>)[1-9][0-9]*')
    }
    matches['Date'] = re.findall(regex_dict['Date'], track)[0]
    matches['Transport'] = re.findall(regex_dict['Transport'], track)
    matches['Distance'] = list(map(int, re.findall(regex_dict['Distance'], track)))
    assert len(matches['Transport']) == len(matches['Distance']), "Different number for transports and distances"
    return matches


def process(filepath):
    timelines = []
    if isinstance(filepath, (tuple, list)):
        for path in filepath:
            timelines.append(process(path))
        return timelines

    kml = read_kml(filepath)
    matches = process_trackstring(kml)
    return matches


def vehicle_props(historic_transportation):
    props = {}

    if isinstance(historic_transportation, dict):
        for idx in range(len(historic_transportation['Transport'])):
            props.update({historic_transportation['Transport'][idx], historic_transportation['Distance'][idx] / 1000})
            return props

    for dic in historic_transportation:
        for idx in range(len(dic['Transport'])):

            vehicle = dic['Transport'][idx]
            if vehicle in props:
                props[vehicle] += dic['Distance'][idx] / 1000
            else:
                props[vehicle] = dic['Distance'][idx] / 1000
    return props


def map_movement_to_vehicle(vehicle_data):
    lookup = {
        'Running': 'Foot',
        'Walking': 'Foot',
        'On the subway': 'Subway and Tram',
        'On a bus': 'Bus',
        'Moving': 'Foot',
        'Driving': 'Car',
        'On a tram': 'Subway and Tram',
        'On a train': 'Train'
    }
    ret = {}
    for key in vehicle_data:
        transport = lookup[key]
        if transport in ret:
            ret[transport] += vehicle_data[key]
        else:
            ret[transport] = vehicle_data[key]
    return ret

