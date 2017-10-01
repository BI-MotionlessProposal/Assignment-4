# Assignment 4: Data Visualisation

### Task 1
Solution (see Solution1.py for runnable script):
*1. Create a plot with the help of Basemap, on which you plot sales records for 2015 which are not farther away than 50km from Copenhagen city center (lat: 55.676111, lon: 12.568333)*

We start by extracting and year and zipcode into numeric values. Two new columns are created 'zip_nr' and 'sell_year' containing our vales to compare sell year and zipcode numerically.


```python
df['zip_nr'] = [int(el.split(' ')[0]) 
                for el in df['zip_code'].values]
df['sell_year'] = df['sell_date'].dt.year
```
Then we calculate the number of kilometres from Copenhagen city with the help of a Harversine function 'def distance(origin, destination):' - taken from lecture class with some modification. We put the values in a new columns 'distance'.
```python
df['distance'] = [distance((55.676111,12.568333), el)for el in df[[ 'lat','lon']].values]
```
We create a mask on the DataFram with some boolean expressions on the new columns. This will be printed on the map.

```python
mask = ((~df.lat.isnull()) & 
        (~df.lon.isnull()) & (df['distance'] <= 50) & 
        (df['sell_year'] == 2015))
```

Ploting the geo coordinates on the BaseMap:

```python
df_cph_00_05_large = df[mask]
x_values = df_cph_00_05_large['lon']
y_values = df_cph_00_05_large['lat']
# create new figure, axes instances.
fig = plt.figure()
ax = fig.add_axes([x_values.min(), y_values.min(), 
                   x_values.max(), y_values.max()])

# setup mercator map projection.
m = Basemap(llcrnrlon=11.2, llcrnrlat=55.1, 
            urcrnrlon=13.1, urcrnrlat=56.2,
            rsphere=(6378137.00, 6356752.3142),
            resolution='h', projection='merc',
            lat_0=40., lon_0=-20., lat_ts=20.)

m.drawcoastlines()
m.fillcontinents(zorder=0)
m.scatter(df_cph_00_05_large.lon.values, 
          df_cph_00_05_large.lat.values, 
          3, marker='o', latlon=True)

# draw parallels
m.drawparallels(np.arange(10, 90,  1), 
                labels=[1, 1, 0, 1])
# draw meridians
m.drawmeridians(np.arange(-180, 180, 1), 
                labels=[1, 1, 0, 1])

```
### Task 2

*2. Use folium to plot the locations of the 1992 housing sales for the city centers of Copenhagen (zip code 1000-1499), Odense (zip code 5000), Aarhus (zip code 8000), and Aalborg (zip code 9000), see Assignment 3 onto a map.*

Solution (see Solution2.py for runnable script):

We extract sell year and zipcode as numeric values just like in previous task. Then we make a long compare statement to get the data we are looking for.

```python
mask = ((df['sell_year'] == 1992) & 
        (~df.lat.isnull()) & 
        (~df.lon.isnull()) & 
        ( ( ( df['zip_nr'] >= 1000 ) & ( df['zip_nr'] <= 1499 ) ) |  
         ( df['zip_nr'] == 5000 ) |  
         ( df['zip_nr'] == 8000 ) | 
         ( df['zip_nr'] == 9000 ) ) 
       )
```
We use folium to display the geocode data on the map
```python
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

```


### Task 3

As a first step the flow of this script processes and modifies data for our needs (modifying zipcode to 4 digits only, as well as casting price_per_sq_m, lon and lat values) and then using haversine function with two input params which are basically four values(norreport lat & long, and target lat long) as a last step, it plots the values and saves as an png file.

### Task 4

The result for this question is in file : "Assignment 4 - 4.ipynb" and solution4.py. Due to some difficulties installing modules with pip or importing them to the project I was forced to use the Jupiter Notebook to write the solutions.

The soluton is simple. First we read the data from the boliga_all_loc.csv then group the values by distinct zipcode. After that it is easy to produce a histogram with sales per zipcode. The output file is in the solution folder.

### Task 5

The result for this question is in file : "Assignment 4 - 5.ipynb" and solution4.py. Due to some difficulties installing modules with pip or importing them to the project I was forced to use the Jupiter Notebook to write the solutions.

Here two steps had to be taken. 
- One order by distinct zipcode 
- Two order by room number per sale but the flow is the same.


```
for zip in unique_zips:
    
    zip_df = df[df['zip_int'] == zip]
    rooms_d = {}      
    
    unique_rooms = df['no_rooms'].unique()
    unique_rooms.sort()
    sales_rooms = collections.OrderedDict()
    for rooms in unique_rooms:
        no_sales = len(df[df['no_rooms'] == rooms])
        sales_rooms[rooms] = no_sales
    
```
The output file is also placed in the result folder

### Task 6
Unfortunately we were unable to finish this task in time since we occured some errors and unexpected behavior.

### Task 7

*7. Freestyle Create a plot, which visualizes a fact hidden in the housing sales data, which you want to highlight to business people.*

This script shows the mean and median price per square meter by construction year for sales records during 2017. This can give an insight to what construction year is "hot" on the market for 2017. The result of the sript is found in result/result_solution_7.png
