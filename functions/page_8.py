import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd
import numpy as np
import plotly.graph_objs as go

from joblib import load

reg_forest_AB = load('ML_models/model_forest_AB.joblib')
reg_forest_joined = load('ML_models/model_forest_joined.joblib')

def page_8_title():
        return dbc.Row(
            [dbc.Col(html.H3("Machine Learning Visualization"), width='auto'),],
             #dbc.Col(html.H4("And Room type"), width='auto')],
            justify='end',
            align='baseline'
        )


def ML_comparison_h():
    features_AB = ['Latitude', 'Longitude', 'Minimum Nights', 'Number of Reviews', 'Reviews per Month', 'Calculated Host Listings count', 'Availability 365', 
                   'Neighbourhood Label', 'Neighbourhood group: Bronx', 'Neighbourhood group: Brooklyn', 'Neighbourhood group: Manhattan', 
                   'Neighbourhood group: Queens', 'Neighbourhood group: Staten Island', 'Room Type: Entire home/apt', 'Room Type: Private room', 'Room Type: Shared room']

    features_joined = features_AB + ['Turistic Places within 2500m', 'Turistic Places within 1000m', 'Turistic Places within 500m', 
                                     'Rat Sightings within 2500m', 'Rat Sightings within 1000m', 'Rat Sightings within 500m', 
                                     'Trees within 2500m', 'Trees within 1000m', 'Trees within 500m'] 
    
    plot_data1 = pd.Series(reg_forest_AB.feature_importances_, index=features_AB).nlargest(30)
    plot_data2 = pd.Series(reg_forest_joined.feature_importances_, index=features_joined).nlargest(30)
    
    data = []
    data.append(go.Bar(y = plot_data1.index, x=plot_data1.values, orientation='h', name="Without Turistic places,<br>Trees and Rats"))
    data.append(go.Bar(y = plot_data2.index, x=plot_data2.values, orientation='h', name="With Turistic places,<br>Trees and Rats"))
    
    layout = {"title": {'text': "Feature importance assigned by two Random Forests fitted on diferent data", 'xanchor': 'center','yanchor': 'top', 'y':0.9, 'x':0.5}, 
              "xaxis": {"title": "Feature importance"},
              "height":700}    
    
    return go.Figure(data=data, layout=layout)

def ML_comparison_v():
    features_AB = ['Latitude', 'Longitude', 'Minimum Nights', 'Number of Reviews', 'Reviews per Month', 'Calculated Host Listings count', 'Availability 365', 
                   'Neighbourhood Label', 'Neighbourhood group: Bronx', 'Neighbourhood group: Brooklyn', 'Neighbourhood group: Manhattan', 
                   'Neighbourhood group: Queens', 'Neighbourhood group: Staten Island', 'Room Type: Entire home/apt', 'Room Type: Private room', 'Room Type: Shared room']

    features_joined = features_AB + ['Turistic Places within 2500m', 'Turistic Places within 1000m', 'Turistic Places within 500m', 
                                     'Rat Sightings within 2500m', 'Rat Sightings within 1000m', 'Rat Sightings within 500m', 
                                     'Trees within 2500m', 'Trees within 1000m', 'Trees within 500m'] 
    
    plot_data1 = pd.Series(reg_forest_AB.feature_importances_, index=features_AB).nlargest(30)
    plot_data2 = pd.Series(reg_forest_joined.feature_importances_, index=features_joined).nlargest(30)
    
    data = []
    data.append(go.Bar(x = plot_data1.index, y=plot_data1.values, orientation='v', name="Without Turistic places, Trees and Rats"))
    data.append(go.Bar(x = plot_data2.index, y=plot_data2.values, orientation='v', name="With Turistic places, Trees and Rats"))
    
    layout = {"title": {'text': "Feature importance assigned by two Random Forests fitted on diferent data", 'xanchor': 'center','yanchor': 'top', 'y':0.9, 'x':0.5}, 
              "yaxis": {"title": "Feature importance"},
              "xaxis": {'dtick': 1, 'tickfont': {'size': 10}, 'tickangle': -80}, 
              "legend":{"orientation": "h", "yanchor": "bottom", "y": 1.02, "xanchor": "right", "x": 1},
              "height":500}    
    
    return go.Figure(data=data, layout=layout)


text1 = """Here we get into the actual machine learning tool that we use for our price estimator. We use something called Random Forest to make a regression analysis on the data that is put into the machine.

The figure illustrates the importance of the features discussed previously, in other words, how much of the price can be explained by a given feature. Hover over a feature to see exact values or inspect it visually to see how they compare.

The blue bars show the features’ importance as assigned by a version of the estimator not using our custom features, and the red bars show how important the different features are according to a second version that were also given the extra features.   
"""

text2 =""""""



def page_8(df):
        return html.Div([
        dbc.Row(
            [
                dbc.Col(dcc.Markdown(text1), width=3),
                dbc.Col((dcc.Graph(id="graph8", figure=ML_comparison_h(), config={'displayModeBar': False})))
            ]
        ),
        dbc.Row(
            [
                dbc.Col(dcc.Markdown(text2),)
            ]
        ),
    ],style={'text-align': 'justify',},)    
    