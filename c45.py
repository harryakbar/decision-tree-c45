import csv
import math

freq_value  = {}
data = {}
target_attr = 'play'

data_entropy = 0

with open('Forecast.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    data = list(reader)

for row in data:
    if(row[target_attr] in freq_value):
        freq_value[row[target_attr]] += 1
    else:
        freq_value[row[target_attr]] = 1

for freq in freq_value.values():
    data_entropy += (-freq/len(data)) * math.log(freq/len(data), 2)


    