import pandas as pd
import math
import collections
from math import radians, cos, sin, asin, sqrt
import matplotlib
import numpy as np
matplotlib.use('Agg') # Must be before importing matplotlib.pyplot or pylab!
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plot
import os


def question6(data):
    modified = pd.DataFrame(data['zip_code'].str.split(' ', 1).tolist(), columns = ['zip', 'full_name'])
    data = data.assign(zip=modified['zip'])
    data['zip'] = pd.to_numeric(data['zip'], errors='coerce')
    data['price_per_sq_m'] = pd.to_numeric(data['price_per_sq_m'], errors='coerce')



    zips = data['zip'].unique()
    zips.sort()
    sales = collections.OrderedDict()

    for zip in zips:
        counting = len(data[data['zip'] == zip])
        sales[zip] = counting


    fig = plot.figure()
    ax = fig.add_subplot(111, projection='3d')
    x = []
    y = []
    for zip, count in sales.items():
        x.append(zip)
        y.append(count)

    histogram, xs, ys = np.histogram2d(x, y)
    xpos, ypos = np.meshgrid(xs[:-1] + xs[1:], ys[:-1] + ys[1:])

    x1 = xpos.flatten()/2
    y1 = ypos.flatten()/2
    z1 = np.zeros_like(xpos)

    xx = xs [1] - xs [0]
    yy = ys [1] - ys [0]
    zz = histogram.flatten()

    ax.bar3d(x1, y1, z1, xx, yy, zz,)

    fig.savefig('./data/foo.png')

if __name__ == "__main__":
    dateparse = lambda x: pd.datetime.strptime(x, '%d-%m-%Y')
    question6(pd.read_csv('./boliga_all_loc.csv', parse_dates=['sell_date'], date_parser = dateparse))
