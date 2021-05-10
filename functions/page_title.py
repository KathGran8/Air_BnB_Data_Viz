import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from functions.page_0 import page_intro_title
from functions.page_1 import page_1_title
from functions.page_2 import page_2_title
from functions.page_3 import page_3_title
from functions.page_4 import page_4_title
from functions.page_5 import page_5_title
from functions.page_6 import page_6_title
from functions.page_7 import page_7_title
from functions.page_8 import page_8_title
from functions.page_9 import page_9_title



def page_title(pathname):
    first_url = (pathname[:32] == '/user/kathgran8-air_bnb_data_viz' and pathname[-12:] == '/proxy/8080/')
    if pathname == "/" or first_url:
        return page_intro_title()
    
    elif pathname == "/page-1":
        return page_1_title()
    
    elif pathname == "/page-2":
        return page_2_title()

    elif pathname == "/page-3":
        return page_3_title()

    elif pathname == "/page-4":
        return page_4_title()
        
    elif pathname == "/page-5":
        return page_5_title()
        
    elif pathname == "/page-6":
        return page_6_title()
        
    elif pathname == "/page-7":
        return page_7_title()
        
    elif pathname == "/page-8":
        return page_8_title()
        
    elif pathname == "/page-9":
        return page_9_title()
        
    # If the user tries to reach a different page, return a 404 message
    #return dbc.Jumbotron(
    #    [
    #        html.H1("404: Not found", className="text-danger"),
    #        html.Hr(),
    #        html.P(f"The pathname {pathname} was not recognised..."),
    #    ]
    #)