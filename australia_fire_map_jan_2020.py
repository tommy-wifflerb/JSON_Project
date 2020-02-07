import csv
from plotly.graph_objs import Scattergeo,Layout
from plotly import offline
# Load file into script
open_file = open('australia_fire_data_january_2020026.txt','r')
csv_file = csv.reader(open_file, delimiter=',')
# Create header index dictionary
header_row = next(csv_file)
l1 = [i for i in range(len(header_row))]
header = dict(zip(header_row,l1))

lats,longs,brightness = [],[],[]
# Propagate lists of latitude, longitude, and brightness
for row in csv_file:
    lat = float(row[header['latitude']])
    long = float(row[header['longitude']])
    bright = float(row[header['brightness']])
    lats.append(lat)
    longs.append(long)
    brightness.append(bright)
# Setup data to plot with scattergeo
data = [{
    'type': 'scattergeo',
    'lon': longs,
    'lat': lats,
    'marker':{
        'size':[0.05*brite for brite in brightness], #this is called list comprehension, 'size' is the key, value would be a list
        'color': brightness,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title':'Brightness'}
        },
}]
# Setup plot layout
my_layout = Layout(title='Australia Fires - January 2020',
                    geo = dict(lonaxis=dict(range=[111,155]),
                    lataxis=dict(range=[-40,-11.7])))

fig = {'data':data, 'layout':my_layout}
# Generate html file
offline.plot(fig,filename='aus_fires_jan_2020.html')
