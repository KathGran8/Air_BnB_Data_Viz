import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

import dash_leaflet as dl
import pandas as pd

def page_5_title():
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
                   min=0,
                   max=10,
                   step=None,
                   marks={0: 'Entire App',
                          5: 'Private Room',
                          10: 'Shared Room'},
                   value=5,
                   included=False),
    ]
)
slider2 = dbc.FormGroup(
    [
        dbc.Label("Slider2", html_for="slider2"),
        dcc.Slider(id="slider2", min=0, max=10, step=0.5, value=3),
    ]
)
slider3 = dbc.FormGroup(
    [
        dbc.Label("Slider3", html_for="slider3"),
        dcc.Slider(id="slider3", min=0, max=10, step=0.5, value=3),
    ]
)

form = dbc.Form([slider1, slider2, slider3])

NYC_coor = (40.730610, -73.935242)
url = 'https://tiles.stadiamaps.com/tiles/alidade_smooth/{z}/{x}/{y}{r}.png'
attribution = '&copy; <a href="https://stadiamaps.com/">Stadia Maps</a> '

map_coord = html.Div([
            html.P("Click on map to choose Coordinate:"),
            dl.Map(id="map-id", style={'width': '100%', 'height': '50vh'}, 
                   center=NYC_coor, zoom=10, children=[dl.TileLayer(url=url, maxZoom=20, attribution=attribution)]),            
            html.Div(id="coordinate-click-id")
            ])

def page_5(df):
    return html.Div([dbc.Row([
                        dbc.Col(html.Div(Sampeltext), width=3),
                        dbc.Col(form, ), #style={'background-color': '#eb4034'}),
                        dbc.Col(map_coord,) #style={'background-color': '#3b968a'})
                    ]),
                    dbc.Row([
                        html.Div(id='slider-output-container'),
                        html.Div(id='coordinate-click-id') 
                    ])])