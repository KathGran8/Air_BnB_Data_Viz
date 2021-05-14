import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd
from scipy.ndimage import gaussian_filter1d
import plotly.graph_objs as go
import base64

def page_6_title():
    return dbc.Row(
            [dbc.Col(html.H3("Understanding the New Features"), width='auto'),],
             #dbc.Col(html.H4("And Room type"), width='auto')],
            justify='end',
            align='baseline'
        )


text1 = """On this page we explore the distribution of *trees*, *rats* and *tourist places* within a 2.5km radius of each Airbnb listing. The figure to the right shows how many listings in the different boroughs are within 2.5 km of a given number of the new features.

It is immediately clear that boroughs have a different number of trees, rats and tourist places. But the figure also shows that our new features are spread unevenly between the different boroughs.
"""

text2 = """In The Bronx, there is a steady increase in the amount of listings as the number of trees increases, while Staten Island has a rather even distribution. The rest of the boroughs have an approximately normal distribution of listings as the number of trees increases, though a dissimilar one at that.

The distribution of rats however skewers things. Not only is the number of rats quite different with Brooklyn having far more sightings, and Queens and Staten Island having very few.

Lastly we have the number of tourist places within 2.5 km of Airbnb listings. This is where things get very uneven. Most boroughs manage around 10 to 20 tourist attractions at the most, but Manhattan tops out around 75-80 places. Showing us where the life of the city is located. Perhaps this is also why Manhattan was so much more expensive than the other boroughs on page 2?"""



def page_6(df, img_scr1):
        return html.Div([
        dbc.Row(
            [
                dbc.Col(dcc.Markdown(text1), width=3),
                dbc.Col(html.Img(src=img_scr1, width = '100%'))
            ]
        ),
        dbc.Row(
            [
                dbc.Col(dcc.Markdown(text2),)
            ]
        ),
    ],style={'text-align': 'justify',},)