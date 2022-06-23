import math
data = [2.2,3.3,4.4,5.5,float('NaN'),float('NaN'),3.5,float('NaN')]
filteredData = []

for i in data:
    if not math.isnan(i):
        filteredData.append(i)

print(filteredData)