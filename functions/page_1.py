import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd
import dash_leaflet as dl

def page_1_title():
        return dbc.Row(
            [dbc.Col(html.H3("Map: Neighbourhoods and Room types"), width='auto'),],
             #dbc.Col(html.H4("And Room type"), width='auto')],
            justify='end',
            align='baseline'
        )

text1 = """The map takes a while to load, but it shows us New York as we know and love it.

The map displays New York colored by its boroughs: Bronx, Brooklyn, Manhattan, Queen and Staten Island, each divided into its smaller neighbourhoods. The map is interactive: You can hover over the map to see the name of the neighbourhoods, and the borough it belongs to. You can also toggle which of the different room types to show, by clicking the boxes in the top right corner of the map.
"""

text2 ="""If you include all the rentals on the maps it is clear to see that most listings are inside of or close to Manhattan, with Bronx and Staten Island having noticeably fewer rentings. Due to so many listings in Manhattan the map also draws a clear square in the middle, surrounding the famous Central Park, where there are no houses to be rented out since it is a park. This theme of parks/green areas being visible by having no listing is also evidenced in Brooklyn's Prospect Park and Green-Wood Cemetery or Queens John F Kennedy International Airport.

Notice how it takes longer to toggle the *entire home/apartment* box than it does the *shared room* box? This is because there are many more instances of entire apartments being rented out than shared rooms, this happens even though the displayed data is only a third of the dataset. 
"""






def page_1(df):
        return html.Div([
        dbc.Row(
            [
                dbc.Col(dcc.Markdown(text1), width=3),
                dbc.Col(html.Iframe(id='map1', srcDoc = open('html_plots/Map_room_type_v2_033.html','r').read(),                                     
                                    width='100%',height = '450'))
            ]
        ),
        dbc.Row(
            [
                dbc.Col(dcc.Markdown(text2),)
            ]
        ),
    ],style={'text-align': 'justify',},)
