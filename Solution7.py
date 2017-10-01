%matplotlib notebook
%matplotlib inline

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

from datetime import date
from datetime import datetime

import warnings
warnings.filterwarnings('ignore')
from mpl_toolkits.basemap import Basemap


dateparse = lambda x: pd.datetime.strptime(x, '%d-%m-%Y')
# A CSV file containing all scraped data, the result of assignment number two
complete_data = './data/boliga_all_loc.csv'
df = pd.read_csv(complete_data, parse_dates=['sell_date'], date_parser=dateparse)

df['zip_nr'] = [int(el.split(' ')[0]) 
                for el in df['zip_code'].values]
df['sell_year'] = df['sell_date'].dt.year



mask = ((df['sell_year'] == 2017) & (df['no_rooms']  == 2) & (df['year_of_construction'] < 1990))
no_rooms_series = df[mask]['year_of_construction']
stats = [(no,
          df[(df['year_of_construction'] == no)]['price_per_sq_m'].mean(), 
          df[(df['year_of_construction'] == no)]['price_per_sq_m'].median()) 
         for no in range(int(no_rooms_series.min()), int(no_rooms_series.max()))]


df_stats = pd.DataFrame(stats, columns=['no_rooms', 'mean_price', 'median_price'])
df_stats

%matplotlib notebook


plt.plot(df_stats.no_rooms, df_stats.mean_price, 
         label="Mean price per sqm")
plt.plot(df_stats.no_rooms, df_stats.median_price, 
         label="Median price per sqm")
plt.legend()

