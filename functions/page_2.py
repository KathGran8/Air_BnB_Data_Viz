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

Sampeltext = "!!!!Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin fermentum euismod commodo. Phasellus metus lorem, tristique nec erat in, laoreet ultricies nunc. Maecenas efficitur placerat lobortis. Nullam lacus lectus, molestie ut semper vel, vestibulum sed ligula.!!"

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


    layout = {"title": {'text': "Mean Price per Room type and Neighbourhood Group", 'xanchor': 'center','yanchor': 'top', 'y':0.9, 'x':0.5},  
              "yaxis": {"title": "Price (dollars)"}} 

    return go.Figure(data=data, layout=layout)




def page_2(df):
        return dbc.Row(
            [
                dbc.Col(html.Div(Sampeltext), width=3),
                dbc.Col((dcc.Graph(id="graph2", figure=make_price_room_ng(df), config={'displayModeBar': False})))
            ]
        )