import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd
import numpy as np
import plotly.graph_objs as go

def page_6_title():
        return dbc.Row(
            [dbc.Col(html.H3("Some plot"), width='auto'),],
             #dbc.Col(html.H4("And Room type"), width='auto')],
            justify='end',
            align='baseline'
        )

Sampeltext = "!!!!Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin fermentum euismod commodo. Phasellus metus lorem, tristique nec erat in, laoreet ultricies nunc. Maecenas efficitur placerat lobortis. Nullam lacus lectus, molestie ut semper vel, vestibulum sed ligula.!!"

def graph_distribution(df):
    plot_data = df.groupby(['availability_365',]).mean().loc[:,'price']

    x = plot_data.index
    y = plot_data.values
    y_smoothed = gaussian_filter1d(y, sigma=3)
    
    data = []
    data.append(go.Scatter(x = x, y = y, name="Data"))
    data.append(go.Scatter(x = x, y = y_smoothed, name="Spline"))
    
    layout = {"title": {'text': "Data and fitted Spline Curve Using Gaussian Smoothing", 'xanchor': 'center','yanchor': 'top', 'y':0.9, 'x':0.5}, 
              "xaxis": {"title": "Availability (days per year)"}, 
              "yaxis": {"title": "Price (dollars)"}}    
    
    return go.Figure(data=data, layout=layout)



def page_6(df, img_scr1):
    return dbc.Row(
            [
                dbc.Col(html.Div(Sampeltext), width=3),
                dbc.Col((dcc.Graph(id="graph3", figure=graph_distribution(df), config={'displayModeBar': False})))
            ]
        )