import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import pandas as pd
import numpy as np

def page_intro_title():
    return dbc.Row(
            [dbc.Col(html.H3("Introduction"), width='auto'),],
             #dbc.Col(html.H4("And Neighbourhood (group)"), width='auto')],
            justify='end',
            align='baseline'
        )

Sampeltext = "!!!!Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin fermentum euismod commodo. Phasellus metus lorem, tristique nec erat in, laoreet ultricies nunc. Maecenas efficitur placerat lobortis. Nullam lacus lectus, molestie ut semper vel, vestibulum sed ligula.!! And here goes the link to the explainer notebook."

def make_tabel(df_head):
    df = df_head.iloc[:8].copy(deep = True)
    df['lat_round'] = np.round(df.latitude,2)
    df['lng_round'] = np.round(df.longitude,2)
    col_id = ['room_type', 'minimum_nights', 'availability_365', 'number_of_reviews', 'reviews_per_month', 'calculated_host_listings_count', 'neighbourhood_group', 'neighbourhood', 'lat_round', 'lng_round']
    col_name = ['Room Type', 'Minimum Nights', 'Availability 365', 'Number of Reviews', 'Reviews per Month', 'Listings of Host', 'Borough', 'Neighbourhood', 'lat', 'lng', ]
    intro_table =  dash_table.DataTable(id='table',
                                   columns=[{"name": name, "id": i} for i,name in zip(col_id,col_name)], #df_head.columns], 
                                   data=df.to_dict('records'),
                                   style_table={'overflowX': 'auto',
                                              'width': '100%'}
                                  )
    return intro_table




def page_intro(df_head):
    return dbc.Row(
            [
                dbc.Col(html.Div(Sampeltext), width=3),
                dbc.Col(make_tabel(df_head), width=9)
            ]
    )