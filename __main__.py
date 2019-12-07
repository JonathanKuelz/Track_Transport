from os import listdir
from process_kml import process

directory = './Bewegungsdaten'
files = listdir(directory)
for i in range(len(files)):
    files[i] = directory + '/' + files[i]
tracking_data = process(files)
print(tracking_data)
