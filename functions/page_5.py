import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd
import dash_leaflet as dl

def page_5_title():
        return dbc.Row(
            [dbc.Col(html.H3("Map: Price and New Features"), width='auto'),],
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


text1 = """While the initial dataset from the Airbnb site is nice and extensive, we promised to take the analysis one step further. Here we do that by introducing the additional datasets.
On the map we have enhanced the initial dataset with three additional datasets of New York. 
The Tree Census in New York City 2015, mapping the more than 684,000 trees of New York.
NYC Rat Sightings, a dataset describing the more than 100,000 rat sightings New York  had from 2010 to 2017. To keep the data relevant, we only select rat sightings from 2017.
A dataset compromising 348 New York Tourist Locations. 
"""

text2 ="""
Again, we have an interactive map: You can toggle the boxes to display the different features. This time, a bar at the top of the map shows the difference in price per night for staying at an Airbnb condo. The color scaling corresponds to the price of the individual listing. 

Notice how Manhattan is a lot more blue and expensive, while Brooklyn is a lot more red, and therefore cheaper. This is despite the many trees in the area. Perhaps the number of trees nearby is not that influential after all? Or perhaps the number of rats which is also high has something to do with it?"""



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
