import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd
import plotly.graph_objs as go

def page_2_title():
    return dbc.Row(
            [dbc.Col(html.H3("Price vs Room type"), width='auto'),],
             #dbc.Col(html.H4("And Neighbourhood (group)"), width='auto')],
            justify='end',
            align='baseline'
        )


def make_price_room_ng(df):
    plot_data = df.groupby(['neighbourhood_group','room_type',]).mean().loc[:,'price']
    
    x = ['Entire home/apt', 'Private room', 'Shared room']
    #ef553b
    data = []
    data.append(go.Scatter(x = x, y = plot_data.loc['Bronx'], name="Bronx", line=dict(dash='dash')))
    data.append(go.Scatter(x = x, y = plot_data.loc['Brooklyn'], name="Brooklyn", line=dict(dash='dash')))
    data.append(go.Scatter(x = x, y = plot_data.loc['Manhattan'], name="Manhattan", line=dict(dash='dash')))
    data.append(go.Scatter(x = x, y = plot_data.loc['Queens'], name="Queens", line=dict(dash='dash')))
    data.append(go.Scatter(x = x, y = plot_data.loc['Staten Island'], name="Staten Island", line=dict(dash='dash')))


    layout = {"title": {'text': "Mean Price per Room type and Borough", 'xanchor': 'center','yanchor': 'top', 'y':0.9, 'x':0.5},  
              "yaxis": {"title": "Price (dollars)"}} 

    return go.Figure(data=data, layout=layout)


text1 = """This figure displays prices for the different rental types on Airbnb, going from renting entire homes/apartments as the generally most expensive option, over renting a private room and the cheapest option, renting a room shared with strangers.

This visual compares the average price per room type (in dollars), for the three types of Airbnb listing, for the five main boroughs in New York. It shows that Manhattan is the most expensive one, with a mean price for *private rooms* (113$) almost as expensive as renting an entire apartment in the cheapest borough, Bronx (127$)!
"""

text2 ="""Try to hover over the dots to see the actual mean price displayed next to them. Small tip, if you mess up the figure, simply double click reset it to the default look again ☺
"""






def page_2(df):
        return html.Div([
        dbc.Row(
            [
                dbc.Col(dcc.Markdown(text1), width=3),
                dbc.Col((dcc.Graph(id="graph2", figure=make_price_room_ng(df), config={'displayModeBar': False})))
            ]
        ),
        dbc.Row(
            [
                dbc.Col(dcc.Markdown(text2),)
            ]
        ),
    ],style={'text-align': 'justify',},)
