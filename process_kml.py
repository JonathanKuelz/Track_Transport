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
        'Transport': re.compile('(?<=\"Category\"><value>)(Running|Walking|On the subway|On a bus|Moving|Driving)(?=<)'),
        'Distance': re.compile('(?<=[a-zA-Z]</value></Data><Data name=\"Distance\"><value>)[1-9][0-9]*')
    }
    matches['Date'] = re.findall(regex_dict['Date'], track)
    matches['Transport'] = re.findall(regex_dict['Transport'], track)
    matches['Distance'] = re.findall(regex_dict['Distance'], track)
    # if len(matches['Transport']) is not len(matches['Distance']):
    #     return False
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