
import pandas as pd
import math
import os
from datetime import date
from datetime import datetime

import warnings
warnings.filterwarnings('ignore')



dateparse = lambda x: pd.datetime.strptime(x, '%d-%m-%Y')
# A CSV file containing all scraped data, the result of assignment number two
complete_data = './boliga_all_loc.csv'
df = pd.read_csv(complete_data, parse_dates=['sell_date'], date_parser=dateparse)

df['zip_nr'] = [int(el.split(' ')[0]) for el in df['zip_code'].values]
df['sell_year'] = df['sell_date'].dt.year

mask = ((df['sell_year'] == 1992) & 
        (~df.lat.isnull()) & 
        (~df.lon.isnull()) & 
        ( ( ( df['zip_nr'] >= 1000 ) & ( df['zip_nr'] <= 1499 ) ) |  
         ( df['zip_nr'] == 5000 ) |  
         ( df['zip_nr'] == 8000 ) | 
         ( df['zip_nr'] == 9000 ) ) 
       )

#df.head()

df_result = df[mask]



import folium


my_map = folium.Map(location=[55.88207495748612, 10.636574309440173], zoom_start=6)

for coords in zip(df_result.lon.values, 
                  df_result.lat.values):
    folium.CircleMarker(location=[coords[1], coords[0]], radius=2).add_to(my_map)
directory = 'result'
if not os.path.exists(directory):
    os.makedirs(directory)    
my_map.save(directory+'/1992_housing_sales_4_cities.html')
my_map

