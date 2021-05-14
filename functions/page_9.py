import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

import dash_leaflet as dl
import pandas as pd

def page_9_title():
        return dbc.Row(
            [dbc.Col(html.H3("Price Suggestion"), width='auto'),],
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
            dl.Map(id="map-id", style={'width': '100%', 'height': '300px'}, 
                   center=NYC_coor, zoom=10, children=[dl.TileLayer(url=url, maxZoom=20, attribution=attribution), 
                                                       dl.LayerGroup(id="layer")])
            ])

text1 = """On this page you can find a suggested price for your own Airbnb listing by moving the sliders to match your condo and clicking on the map to indicate the location.

We recommend choosing the position of your condo first, by navigating the map and zooming to its location and clicking. This way you can see the increase or decrease in price as you adjust how much of your condo you want to rent out, for how long, and if you need to buy a botnet to leave reviews on your listing to inflate the price.
"""

text2 ="""Behind the scenes our machine learning algorithms calculate how much the features you were introduced to on the previous pages increase or decrease the mean price of a condo in a given New York location. 
When you click on the map and adjust the sliders the page gives you a suggested price, this will be an approximation of a likely price in that position with the given parameters."""


def page_9(df):
    return html.Div([dbc.Row([
                        dbc.Col(dcc.Markdown(text1), width=3),
                        dbc.Col([
                            dbc.Row([dbc.Col(form),dbc.Col(map_coord)]),
                            dbc.Row(html.H4(id='prediction'), justify='center', style={'margin-top':'15px'})
                        ])
                    ]),
                    dbc.Row(dbc.Col(dcc.Markdown(text2)),
                            style={'margin-top':'15px'}
                           )], 
                    style={'text-align': 'justify'})

