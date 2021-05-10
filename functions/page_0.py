import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import pandas as pd

def page_intro_title():
    return dbc.Row(
            [dbc.Col(html.H3("Introduction"), width='auto'),],
             #dbc.Col(html.H4("And Neighbourhood (group)"), width='auto')],
            justify='end',
            align='baseline'
        )

Sampeltext = "!!!!Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin fermentum euismod commodo. Phasellus metus lorem, tristique nec erat in, laoreet ultricies nunc. Maecenas efficitur placerat lobortis. Nullam lacus lectus, molestie ut semper vel, vestibulum sed ligula.!!"

def make_tabel(df_head):
    intro_table =  dash_table.DataTable(id='table',
                                   columns=[{"name": i, "id": i} for i in df_head.columns], 
                                   data=df_head.to_dict('records'),
                                   style_cell={'overflow': 'hidden',
                                               'textOverflow': 'ellipsis',
                                               'maxWidth': 0
                                              }
                                  )
    return intro_table




def page_intro(df_head):
    return dbc.Row(
            [
                dbc.Col(html.Div(Sampeltext), width=3),
                dbc.Col(make_tabel(df_head))
            ]
    )