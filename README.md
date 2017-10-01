# Assignment 4: Data Visualisation

## Task

1. Create a plot with the help of Basemap, on which you plot sales records for 2015 which are not farther away than 50km from Copenhagen city center (lat: 55.676111, lon: 12.568333)

We start by extractring and year and zipcode into numeric values. Two new columns are created 'zip_nr' and 'sell_year' containing.


```python
df['zip_nr'] = [int(el.split(' ')[0]) 
                for el in df['zip_code'].values]
df['sell_year'] = df['sell_date'].dt.year
```
Then we calculate the number of kilometres from Copenhagen city with the help of a function. We put the values in a new columns 'distance'.
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

```

2. Use folium to plot the locations of the 1992 housing sales for the city centers of Copenhagen (zip code 1000-1499), Odense (zip code 5000), Aarhus (zip code 8000), and Aalborg (zip code 9000), see Assignment 3 onto a map.

3. Create a 2D plot, which compares prices per square meter (on the x-axis) and distance to Nørreport st. (y-axis) for all housing on Sjæland for the year 2005 and where the zip code is lower than 3000 and the price per square meter is lower than 80000Dkk. Describe in words what you can read out of the plot. Formulate a hypothesis on how the values on the two axis might be related.

4. Create a histogram (bar plot), which visualizes the frequency of house trades per zip code area corresponding to the entire dataset of housing sale records.

5. Create a cumulatve histogram, which visualizes the frequency of house trades per zip code area corresponding to the entire dataset of housing sale records and the vertical bars are colored to the frequency of rooms per sales record. That is, a plot similar to the following, where single rooms are in the bottom and two room frequencies on top, etc. See, http://matplotlib.org/1.3.0/examples/pylab_examples/histogram_demo_extended.html for example.

6. Now, you create a 3D histogram, in which you plot the frequency of house trades per zip code area as a 'layer' for every in the dataset, see http://matplotlib.org/examples/mplot3d/index.html for an example.

7. Freestyle Create a plot, which visualizes a fact hidden in the housing sales data, which you want to highlight to business people.