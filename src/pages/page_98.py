import dash
from dash import Dash, dcc, html
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

future = ["Tables", "Forms", "Connecting to a Mongo Database", "Performing full CRUD operations on the DB",
          "Client-Side Callbacks", "Live stock market page - Update every 5 minutes", "Download file functionality",
          "Upload file functionality", "Full financial dashboard", "Create PDF's", "Create Excel Files",
          "Turning your Dash app into a Progressive Web App"]

for x, i in enumerate(future, 1):
    html.P(f"{i}. {x}")

dash.register_page(__name__, name="Future Plans", title="Future")

layout = html.Div([
    html.P('Plans for this app. In no particular order.',
           style={"fontWeight": "bold", "color": "white", "marginLeft": 140}),
    html.Br(),
    html.Ol([
        html.Li(f'{field}.')
        for field in future
    ], style={"width": "100%", "textAlign": "left", "marginLeft": 140})

])
