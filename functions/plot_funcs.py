import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import plotly.graph_objs as go

import pandas as pd
import numpy as np
from scipy.ndimage import gaussian_filter1d


df = pd.read_csv("Data/data_air/AB_data_clean.csv")
df_head = df.head().iloc[:, :14]

manual_colors = ['#636efa', '#ef553b', '#00cc96']

def make_tabel():
    intro_table =  dash_table.DataTable(id='table',
                                   columns=[{"name": i, "id": i} for i in df_head.columns], 
                                   data=df_head.to_dict('records'),
                                   style_cell={'overflow': 'hidden',
                                               'textOverflow': 'ellipsis',
                                               'maxWidth': 0
                                              }
                                  )
    return intro_table




def make_price_room_ng():
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


def graph_price_avail():
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


def graph_price_neigh_room():
    plot_data = df.groupby(['neighbourhood_other',]).mean().loc[:,'price'].sort_values(ascending = False)
    plot_data_color = df.groupby(['neighbourhood_other',]).mean()[['room_type_Entire home/apt', 'room_type_Shared room', 'room_type_Private room']]
    color = []
    for x in plot_data_color.values:
      color.append(np.argmax(x))
    plot_data_color['color'] = color

    plot_data = pd.DataFrame(plot_data).merge(plot_data_color, left_index = True, right_index = True)

    x = plot_data.index
    y = plot_data.price
    
    data = []
    count_0 = 0; count_1 = 0; count_2 = 0
    for i in range(len(x)):
        if plot_data.color[i] == 0:
            color = '#636efa'
            if count_0 == 0:
                name = 'Entire home/apt'
                data.append(go.Bar(x = [x[i]], y = [y[i]], marker_color = color, name = name))
                count_0 += 1
            else:
                data.append(go.Bar(x = [x[i]], y = [y[i]], marker_color = color, showlegend=False))
                
        elif plot_data.color[i] == 1:
            color = '#00cc96'
            if count_1 == 0:
                name = 'Shared room'
                data.append(go.Bar(x = [x[i]], y = [y[i]], marker_color = color, name = name))
                count_1 += 1
            else:
                data.append(go.Bar(x = [x[i]], y = [y[i]], marker_color = color, showlegend=False))   
                
        elif plot_data.color[i] == 2:
            color = '#ef553b'
            if count_2 == 0:
                name = 'Private room'
                data.append(go.Bar(x = [x[i]], y = [y[i]], marker_color = color, name = name))
                count_2 += 1
            else:
                data.append(go.Bar(x = [x[i]], y = [y[i]], marker_color = color, showlegend=False))   
        
        
    layout = {"title": {'text': "Mean listing price per neighbourhood (also most available listing type)", 'xanchor': 'center','yanchor': 'top', 'y':0.9, 'x':0.5}, 
              "xaxis": {'dtick': 1, 'tickfont': {'size': 10}, 'tickangle': -80}, 
              "yaxis": {"title": "Price (dollars)"},
              "legend":{"orientation": "h", "yanchor": "bottom", "y": 1.02, "xanchor": "right", "x": 1},
              "height": 500}    
    
    return go.Figure(data=data, layout=layout)




