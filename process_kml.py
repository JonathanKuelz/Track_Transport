import re

from pykml import parser as kml_parser
from lxml import etree


def read_kml(filepath):
    with open(filepath, 'rt', encoding='utf-8') as kml:
        track_kml = kml_parser.parse(kml)

    track = etree.tostring(track_kml, pretty_print=True)
    return str(track)


def process_trackstring(track):
    regex_dict = {
        'Date': re.compile("(?<=Location history from )([0-9]{4}-[0-9]{2}-[0-9]{2}) to ([0-9]{4}-[0-9]{2}-[0-9]{2})"),
        'Motion': re.compile("(?<=<name>)(Running|Walking|On the subway|On a bus|)(?=</name>)")
    }
    for key in regex_dict:
        match = re.findall(regex_dict[key], track)


def process(filepath):
    kml = read_kml(filepath)
    process_trackstring(kml)

    t1 = {
        'Date', "2019-11-03"
        'Transport', ["Walking", "Running", "On the subway"],
        'Distance', [2, 13.2, 19]
    }
    t2 = {
        'Date', "2019-12-05"
                'Transport', ["On the subway", "Running", "On a bus"],
        'Distance', [2, 0, 55]
    }
    timelines = [t1, t2]

    return timelines