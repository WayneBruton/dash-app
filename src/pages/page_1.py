import dash
from dash import dcc, html, Input, Output, callback
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

# META TAGS TITLE / IMAGE / DESCRIPTION
dash.register_page(__name__, path="/", name='Home', title='Index', image='page_1.png',
                   description='An Awesome App')

# Page 1 Data


layout = html.Div([
    dbc.Row([
        dbc.Col([
            # html.Br(),
            html.P('Plotly Dash for Python', style={"fontSize": 25, "color": "lime"}),
            # html.Br(),
            html.P('As a recent convert to python, I was searching for a way to visualize data and display it.'
                   ' I discovered Plotly Dash and found it quite amazing. The only way I can describe it is '
                   '"A perfect marriage between Python and Javascript".'),
            # html.Br(),
            html.P('I found not just a tool to visualize data but a way an entire web app can be written with minimum '
                   'code as well as being fast and efficient. Using just Python.'),
            # html.Br(),
            html.P("I will attempt to showcase this here. This is not just about showcasing but rather about my "
                   "learning curve & my progression as a developer. Check out the 'Future Plans' Page to see what I "
                   "plan going forward."),
            # html.Br(),
            html.P("I would never have learned what I have without Adam from the youtube channel 'Charming Data', "
                   "I would highly recommending subscribing.", style={"marginBottom": 75})

        ], width=6, style={"textAlign": "center"}),
        dbc.Col([
            html.Img(src="assets/toad-in-whitch-hat-clipart-md.png", width='50%')
        ], width=6, style={"textAlign": "center"})
    ])

]
)

