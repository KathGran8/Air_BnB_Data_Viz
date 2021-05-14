import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd
from scipy.ndimage import gaussian_filter1d
import plotly.graph_objs as go

def page_4_title():
    return dbc.Row(
            [dbc.Col(html.H3("Price vs Avalibility"), width='auto'),],
             #dbc.Col(html.H4("And Room type"), width='auto')],
            justify='end',
            align='baseline'
        )

def graph_price_avail(df):
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



text1 = """On page 2 we learned how location and rental type changed the price of a condo. But these two things are hard to change when you already own an apartment. Here we look at the relation between the price on an Airbnb listing and the days per year it is available for renting, which is easier for a host to change. 

On the graph we have two lines, the blue line *Data* displaying the mean price of actual Airbnb listings and a red line called *Spline*, showing a smoothed version of the *Data* line, helping us spot the trend in the data.  
"""

text2 ="""Thus the figure shows a general trend of rents, being more expensive when available for more nights of the year, with a notable drop around 275 days per year. Why? Our hypothesis is that the price goes up with higher availability, as there is a higher chance to hit high season times, holidays etc. Why the dip then? Either it could be that private owners want the best days of the year for themselves and therefore only rent out at the less popular times. Or it could be that only commercial hosts are able to maintain such a high availability and they are able to maintain a cheaper price per night with a smaller operating cost."""

def page_4(df):
        return html.Div([
        dbc.Row(
            [
                dbc.Col(dcc.Markdown(text1), width=3),
                dbc.Col((dcc.Graph(id="graph4", figure=graph_price_avail(df), config={'displayModeBar': False})))
            ]
        ),
        dbc.Row(
            [
                dbc.Col(dcc.Markdown(text2),)
            ]
        ),
    ],style={'text-align': 'justify',},)