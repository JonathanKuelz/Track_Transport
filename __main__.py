from os import listdir
from process_kml import process
from calc_co2 import counter_day, counter_timeline

directory = './Bewegungsdaten'
files = listdir(directory)
for i in range(len(files)):
    files[i] = directory + '/' + files[i]
tracking_data = process(files)
print(tracking_data)
print(counter_timeline(tracking_data))



