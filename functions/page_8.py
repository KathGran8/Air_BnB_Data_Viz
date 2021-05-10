import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd
import numpy as np
import plotly.graph_objs as go

def page_8_title():
        return dbc.Row(
            [dbc.Col(html.H3("Machine Learning Visualization"), width='auto'),],
             #dbc.Col(html.H4("And Room type"), width='auto')],
            justify='end',
            align='baseline'
        )

Sampeltext = "!!!!Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin fermentum euismod commodo. Phasellus metus lorem, tristique nec erat in, laoreet ultricies nunc. Maecenas efficitur placerat lobortis. Nullam lacus lectus, molestie ut semper vel, vestibulum sed ligula.!!"

def graph_price_neigh_room(df):
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



def page_8(df):
    return dbc.Row(
            [
                dbc.Col(html.Div(Sampeltext), width=3),
                dbc.Col()#(dcc.Graph(id="graph3", figure=graph_price_neigh_room(df), config={'displayModeBar': False})))
            ]
        )