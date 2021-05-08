import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from functions.page_intro import page_intro_title
from functions.page_1 import page_1_title
from functions.page_2 import page_2_title
from functions.page_3 import page_3_title
from functions.page_4 import page_4_title
from functions.page_5 import page_5_title


def page_title(pathname):
    if pathname == "/":
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
        
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )