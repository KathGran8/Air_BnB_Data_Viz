import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd
import dash_leaflet as dl

def page_5_title():
        return dbc.Row(
            [dbc.Col(html.H3("Map: Price and new features"), width='auto'),],
             #dbc.Col(html.H4("And Room type"), width='auto')],
            justify='end',
            align='baseline'
        )




def page_7(df):
    return dbc.Row(
            [
                dbc.Col(html.Div(Sampeltext), width=3),
                dbc.Col(html.Iframe(id='map1', srcDoc = open('html_plots/Map_features.html','r').read(),                                             width='100%',height = '450'))
            ]
        )


text1 = """!!!!Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin fermentum euismod commodo. Phasellus metus lorem, tristique nec erat in, laoreet ultricies nunc. Maecenas efficitur placerat lobortis. Nullam lacus lectus, molestie ut semper vel, vestibulum sed ligula.!!
"""

text2 =""""""



def page_5(df):
        return html.Div([
        dbc.Row(
            [
                dbc.Col(dcc.Markdown(text1), width=3),
                dbc.Col(html.Iframe(id='map5', srcDoc = open('html_plots/Map_features.html','r').read(),
                                    width='100%',height = '450'))
            ]
        ),
        dbc.Row(
            [
                dbc.Col(dcc.Markdown(text2),)
            ]
        ),
    ],style={'text-align': 'justify',},)
