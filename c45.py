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


def remainder(self, parameter_list):
    s = 0 # sum
    for v in utils.deldup(table[res_col]):
        p = freq(table, res_col, v) / float(len(table[res_col]))
        s += p * math.log(p, 2)
    return -s
print(data_entropy)