import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd
from scipy.ndimage import gaussian_filter1d
import plotly.graph_objs as go
import base64

def page_6_title():
    return dbc.Row(
            [dbc.Col(html.H3("Distribution of new features"), width='auto'),],
             #dbc.Col(html.H4("And Room type"), width='auto')],
            justify='end',
            align='baseline'
        )


text1 = """!!!!Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin fermentum euismod commodo. Phasellus metus lorem, tristique nec erat in, laoreet ultricies nunc. Maecenas efficitur placerat lobortis. Nullam lacus lectus, molestie ut semper vel, vestibulum sed ligula.!!
"""

text2 =""""""



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