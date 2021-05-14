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

text1 = """
Welcome to the page. Here we explore what affects prices of Airbnb apartments in New York and on the last page we let you price your Airbnb apartment or room using our machine learning algorithm.

To understand the analysis and visualisations on these pages, simply go through the pages in the listed fashion by clicking the numbers on the top of the screen. This also serves as a tutorial to equip you with the necessary knowledge to understand the price setting machine on the final tab.

Our analysis of AirBnB pricing uses information from almost 50,000 documented listings in the New York area from 2019, which are available [here](https://www.kaggle.com/dgomonov/new-york-city-airbnb-open-data). 
The dataset features information such as *location of apartments*, *minimum nights per stay*, *nights available per year* and *number of reviews* the listing already has.
We take it one step further and include additional features from the cityscape. Do more trees create a prettier and more expensive neighborhood? Do listings right next door to tourist attractions cost more to rent? Or is an area plagued by rats less popular? Stick around to find out. 
"""

text2 = """A preview of the Airbnb dataset is shown to the right; use the slider in the bottom of the panel to see the features that are relevant for this work.  
"""

text3 = """Page 1 is a map of New York showing where the different neighborhoods are located and the borough they belong to. Additionally, it is possible to interact with it to show the locations of listings from the Airbnb dataset, grouped by their type of room. This will be our starting point.

Pages 2-4 provide a visualization of how different aspects of a place influence the rental price of an Airbnb listing by using the data that was provided in the dataset already presented. 

In Page 5-6,  data exploration is done on three additional datasets, namely a record of location of the trees, rats sightings and touristic places in NYC. Page 5 provides another interactive map with a sample above mentioned data, together with a colour-dependent representation of the price of Airbnb listings. In page 7, it is explored if there is any relation between this extra information and the price of an Airbnb listing. 

Finally, pages 8 and 9 belong to machine learning. The first page analyzes the relevance of the different features that the Airbnb dataset provides with and without the additional datasets information. The second and final page presents the price estimator built with the help of all the previous analysis of the data.

Documentation of the analysis can be found in this [explainer notebook](https://github.com/KathGran8/Air_BnB_Data_Viz/tree/main/Explainer/How_to.ipynb).
"""



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
    return html.Div([
        dbc.Row(
            [
                dbc.Col(dcc.Markdown(text1),)
            ]
        ),
        dbc.Row(
            [
                dbc.Col(dcc.Markdown(text2), width=3),
                dbc.Col(make_tabel(df_head), width=9, align = 'center')
            ]
        ),
        dbc.Row(
            [
                dbc.Col(html.H4('Website Overveiw'))
            ]
        ),
        dbc.Row(
            [
                dbc.Col(dcc.Markdown(text3),)
            ]
        ),
    ],style={'text-align': 'justify',},)
        