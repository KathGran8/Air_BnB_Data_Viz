import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

import dash_leaflet as dl
import pandas as pd

def page_9_title():
        return dbc.Row(
            [dbc.Col(html.H3("Pediction"), width='auto'),],
             #dbc.Col(html.H4("And Room type"), width='auto')],
            justify='end',
            align='baseline'
        )

Sampeltext = "!!!!Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin fermentum euismod commodo. Phasellus metus lorem, tristique nec erat in, laoreet ultricies nunc. Maecenas efficitur placerat lobortis. Nullam lacus lectus, molestie ut semper vel, vestibulum sed ligula.!!"


slider1 = dbc.FormGroup(
    [
        dbc.Label("Room Type", html_for="slider1"),
        dcc.Slider(id="slider1", 
                   min=0, max=10,
                   step=None, value=5,
                   marks={0: 'Entire App',
                          5: 'Private Room',
                          10: 'Shared Room'},
                   included=False),
    ]
)
slider2 = dbc.FormGroup(
    [
        dbc.Label("Minimum Nights", html_for="slider2"),
        dcc.Slider(id="slider2", 
                   min=1, max=365, 
                   step=1, value=183, 
                   marks={1: '1',
                          365: '365'},
                   tooltip={'always_visible':False, 'placement':'bottom'},
                   included=False),
    ]
)
slider3 = dbc.FormGroup(
    [
        dbc.Label("Avalibility", html_for="slider3"),
        dcc.Slider(id="slider3", 
                   min=1, max=365, 
                   step=1, value=183, 
                   marks={1: '1',
                          365: '365'},
                   tooltip={'always_visible':False, 'placement':'bottom'},
                   included=False),
    ]
)
slider4 = dbc.FormGroup(
    [
        dbc.Label("Number of Reviews", html_for="slider4"),
        dcc.Slider(id="slider4", 
                   min=1, max=629, 
                   step=1, value=315, 
                   marks={1: '1',
                          629: '629'},
                   tooltip={'always_visible':False, 'placement':'bottom'},
                   included=False),
    ]
)

form = dbc.Form([slider1, slider2, slider3, slider4])

NYC_coor = (40.730610, -73.935242)
#url = 'https://tiles.stadiamaps.com/tiles/alidade_smooth/{z}/{x}/{y}{r}.png'
#attribution = '&copy; <a href="https://stadiamaps.com/">Stadia Maps</a> 

url = 'https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png'
attribution = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>'
	

map_coord = html.Div([
            html.P("Click on map to choose Coordinate:"),
            dl.Map(id="map-id", style={'width': '100%', 'height': '50vh'}, 
                   center=NYC_coor, zoom=10, children=[dl.TileLayer(url=url, maxZoom=20, attribution=attribution), 
                                                       dl.LayerGroup(id="layer")])
            ])

def page_9(df):
    return html.Div([dbc.Row([
                        dbc.Col(html.Div(Sampeltext), width=3),
                        dbc.Col(form, ), #style={'background-color': '#eb4034'}),
                        dbc.Col(map_coord,) #style={'background-color': '#3b968a'})
                    ]),
                    dbc.Row([
                        dbc.Col(html.H4(id='prediction'), width='auto')
                        #html.Div(id='slider-output-container'),
                        #html.Div(id='coordinate-click-id') 
                    ],
                        justify='center',
                        align='baseline',
                        style={'margin-top':'15px'})])