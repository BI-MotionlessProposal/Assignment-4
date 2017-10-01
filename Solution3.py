import pandas as pd
import math
import collections
from math import radians, cos, sin, asin, sqrt
import matplotlib
matplotlib.use('Agg') # Must be before importing matplotlib.pyplot or pylab!
import matplotlib.pyplot
import os


def question3(data):
    modified = pd.DataFrame(data['zip_code'].str.split(' ', 1).tolist(), columns = ['zip', 'full_name'])
    data = data.assign(zip=modified['zip'])
    data['zip'] = pd.to_numeric(data['zip'], errors='coerce')
    data['lat'] = pd.to_numeric(data['lat'], errors='coerce')
    data['lon'] = pd.to_numeric(data['lon'], errors='coerce')
    data['price_per_sq_m'] = pd.to_numeric(data['price_per_sq_m'], errors='coerce')

    data1 = data[data['sell_date'].dt.year == 2017]
    data2 = data1[data['zip']<=3000]
    data3 = data2[data['price_per_sq_m'] <= 80.000]

    nlon = 55.68
    nlat = 12.57

    #data = data3.assign(norreport_distance=haversine(nlon, nlat, data['lon'], data['lat']))
    data['norreport_distance'] = [distance((nlon,nlat), el)for el in data[[ 'lat','lon']].values]


    y = data['norreport_distance'].values
    x = data['price_per_sq_m'].values


    matplotlib.pyplot.scatter(x, y)

    matplotlib.pyplot.show()
    matplotlib.pyplot.savefig('foo.png')



def distance(origin, destination):
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6371 # km

    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c

    return d

if __name__ == "__main__":
    dateparse = lambda x: pd.datetime.strptime(x, '%d-%m-%Y')
    question3(pd.read_csv('./boliga_all_loc.csv', parse_dates=['sell_date'], date_parser = dateparse))
    
print('end')    
