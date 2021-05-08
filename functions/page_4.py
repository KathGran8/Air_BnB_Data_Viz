import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd

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