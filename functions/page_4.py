import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd
import dash_leaflet as dl

def page_4_title():
        return dbc.Row(
            [dbc.Col(html.H3("Map: Neighbourhoods and Room types"), width='auto'),],
             #dbc.Col(html.H4("And Room type"), width='auto')],
            justify='end',
            align='baseline'
        )

Sampeltext = "!!!!Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin fermentum euismod commodo. Phasellus metus lorem, tristique nec erat in, laoreet ultricies nunc. Maecenas efficitur placerat lobortis. Nullam lacus lectus, molestie ut semper vel, vestibulum sed ligula.!!"







def page_4(df):
    return dbc.Row(
            [
                dbc.Col(html.Div(Sampeltext), width=3),
                dbc.Col(html.Iframe(id='map1', srcDoc = open('html_plots/Map_room_type.html','r').read(),                                     
                                    width='100%',height = '450'))
            ]
        )



"""
NYC_coor = (40.730610, -73.935242)
url = 'https://tiles.stadiamaps.com/tiles/alidade_smooth/{z}/{x}/{y}{r}.png'
attribution = '&copy; <a href="https://stadiamaps.com/">Stadia Maps</a> '

df = pd.read_csv("Data/data_air/AB_data_clean.csv")

manual_colors = ['#636efa', '#ef553b', '#00cc96']


#creating to different marker groups, one for each time period
Entire = []#dl.featureGroup(name='<span style=\\"color: manual_colors[0];\\">Entire home/apt</span>')
Private = []#dl.featureGroup(name='<span style=\\"color: manual_colors[1];\\">Private Room</span>')
Shared = []#dl.featureGroup(name='<span style=\\"color: manual_colors[2];\\">Shared Room</span>')

NYC_coor = (40.730610, -73.935242)

def add_marker_Entire(x):
      Entire.append(dl.CircleMarker(center=[x.latitude, x.longitude], radius= 0.5, color=manual_colors[0], weight = 2,  ))#fill_color=manual_colors[0], fill=True, fill_opacity=1))

def add_marker_Private(x):
      Private.append(dl.CircleMarker(center=[x.latitude, x.longitude], radius= 0.5, color=manual_colors[1], weight = 2,  ))#fill_color=manual_colors[1], fill=True, fill_opacity=1))

def add_marker_Shared(x):
      Shared.append(dl.CircleMarker(center=[x.latitude, x.longitude], radius= 0.5, color=manual_colors[2], weight = 2,  ))#fill_color=manual_colors[2], fill=True, fill_opacity=1))


#apply the function we just created to every row in the dataframe
df[df.room_type == 'Entire home/apt'].apply(lambda x:  add_marker_Entire(x), axis =1)
df[df.room_type == 'Private room'].apply(lambda x:  add_marker_Private(x), axis =1)
df[df.room_type == 'Shared room'].apply(lambda x:  add_marker_Shared(x), axis =1)
#add borh marker groups to the map


map_ny =dl.Map([
    dl.LayersControl(
        [dl.BaseLayer(dl.TileLayer(url=url, attribution=attribution))] +
        [dl.Overlay(dl.LayerGroup(Entire), name="markers", checked=True),
         dl.Overlay(dl.LayerGroup(Private), name="polygon", checked=True)]
    )
], center=NYC_coor, zoom=10)
"""
