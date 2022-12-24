import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data/all_day.json'

with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']

mags, lons, lats, titles = [], [], [], []

for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title'] 
    if mag >= 0:
        mags.append(mag)
        lons.append(lon)
        lats.append(lat)
        titles.append(title)

data = [{
    'type':'scattergeo',
    'lon':lons,
    'lat':lats,
    'text':titles,
    'marker': {
        'size':[5*mag for mag in mags],
        'color': mags,
        'colorscale':'Viridis',
        'reversescale':True,
        'colorbar':{'title':'Magnitude'}
        }
    }]
my_layout = Layout(title='Global Earthquakes')

fig = {'data':data, 'layout':my_layout}
offline.plot(fig, filename='global_earthquakes.html')