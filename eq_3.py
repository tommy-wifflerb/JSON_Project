import json

in_file = open('eq_data_30_day_m1.json','r')
out_file = open('readable_eq_data.json','w')

eq_data = json.load(in_file)
print(type(eq_data))
json.dump(eq_data,out_file,indent=4)

list_of_eqs = eq_data['features']

print(type(list_of_eqs))

print(len(list_of_eqs))

mags, longs, lats, hovertexts = [],[],[],[]

for eq in list_of_eqs:
    mag = eq['properties']['mag']
    lon = eq['geometry']['coordinates'][0]
    lat = eq['geometry']['coordinates'][1]
    hovertext = eq['properties']['title'] #adds title for hovertext
    mags.append(mag)
    longs.append(lon)
    lats.append(lat)
    hovertexts.append(hovertext)

print(mags[:10])

from plotly.graph_objs import Scattergeo,Layout
from plotly import offline

# data = [Scattergeo(lon=longs, lat=lats)]

data = [{
    'type': 'scattergeo',
    'lon': longs,
    'lat': lats,
    'text': hovertexts,
    'marker':{
        'size':[5*mag for mag in mags], #this is called list comprehension, size is the key, value would be a list
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title':'Magnitude'}
        },
}]

my_layout = Layout(title='Global Earthquakes')

fig = {'data':data, 'layout':my_layout}

offline.plot(fig,filename='global_earthquakes.html')