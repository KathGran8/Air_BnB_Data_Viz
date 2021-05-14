import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd
import numpy as np
import plotly.graph_objs as go

def page_7_title():
        return dbc.Row(
            [dbc.Col(html.H3("Price vs New Features"), width='auto'),],
             #dbc.Col(html.H4("And Room type"), width='auto')],
            justify='end',
            align='baseline'
        )


text1 = """This time, the average price in a borough is plotted against the number of trees, rats and tourist places in a 2.5 kilometer radius. 

Although it was expected to find a strong relation between the rental price and the number of trees in the surroundings, the *Spline*, as named and explained in page 4 looks, reasonably constant for all amounts of trees in the first column of plots, which means that even if a condo has 7000 or 1000 trees nearby, the rental price will be similar.
"""

text2 ="""However, the second column of plots shows that the number of rats do have an impact on the rental price of the different listings. Taking Manhattan as an example (3rd row, 2nd column), it can be observed how the price is going down as the number of rats sighted within a radius of 2.5km increases.

The last column in the figure plots price in function of the number of tourist places nearby. Here especially the graphs for Brooklyn, Manhattan, and even Queens, depict how being located near several tourist spots increases the price of a condo. As an example, the graph for Brooklyn (2nd row, 3rd column) shows how the average price of a condo can go from 200$ to 300$ if the number of tourist places within 2.5km goes from 25 to 55.
"""



def page_7(df, img_scr2):
        return html.Div([
        dbc.Row(
            [
                dbc.Col(dcc.Markdown(text1), width=3),
                dbc.Col(html.Img(src=img_scr2, width = '100%'))
            ]
        ),
        dbc.Row(
            [
                dbc.Col(dcc.Markdown(text2),)
            ]
        ),
    ],style={'text-align': 'justify',},)    
    