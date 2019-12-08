from os import listdir
from process_kml import process, vehicle_props, map_movement_to_vehicle, order_dicts
from calc_co2 import counter_timeline
import json

directory = './Bewegungsdaten'
files = listdir(directory)
for i in range(len(files)):
    files[i] = directory + '/' + files[i]
tracking_data = process(files)

emission = order_dicts(counter_timeline(tracking_data))
vehicle_util = map_movement_to_vehicle(vehicle_props(tracking_data))

with open('transportation_emission.json', 'w') as fp:
    json.dump(emission, fp)
with open('transportation_mileage.json', 'w') as fp:
    json.dump(vehicle_util, fp)
