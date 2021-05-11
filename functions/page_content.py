import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from functions.page_0 import page_intro
from functions.page_1 import page_1
from functions.page_2 import page_2
from functions.page_3 import page_3
from functions.page_4 import page_4
from functions.page_5 import page_5
from functions.page_6 import page_6
from functions.page_7 import page_7
from functions.page_8 import page_8
from functions.page_9 import page_9



import pandas as pd

df = pd.read_csv("Data/AB_data_clean.csv")
df_head = df.head().iloc[:, :14]


def page_content(pathname):
    first_url = (pathname[:32] == '/user/kathgran8-air_bnb_data_viz' and pathname[-12:] == '/proxy/8080/')
    if pathname == "/" or first_url:
        return page_intro(df_head)

    elif pathname == "/page-1":
        return page_1(df)
    
    elif pathname == "/page-2":
        return page_2(df)
    
    elif pathname == "/page-3":
        return page_3(df)
    
    elif pathname == "/page-4":
        return page_4(df)

    elif pathname == "/page-5":
        return page_5(df)
    
    elif pathname == "/page-6":
        return page_6(df)
    
    elif pathname == "/page-7":
        return page_7(df)
    
    elif pathname == "/page-8":
        return page_8(df)
    
    elif pathname == "/page-9":
        return page_9(df)
    
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )

