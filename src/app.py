import dash
from dash import Dash, dcc, html
# import pandas as pd
# import plotly.express as px
import dash_bootstrap_components as dbc

app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.SLATE])
server = app.server

sidebar = dbc.Nav([
    dbc.NavLink([
        html.Div(page['name'], className='ms-2'),

    ],
        href=page['path'],
        active='exact'
    )
    for page in dash.page_registry.values()

],
    vertical=True,
    pills=True,
    className='bg-dark')

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.Div('The Eccentric Toad',
                         style={"fontSize": 50, "textAlign": "center", "color": "lime", "fontFamily": "fantasy",
                                "margin-top": 25}),
                width=12),
        dbc.Col(html.Div('A showcase',
                         style={"fontSize": 30, "textAlign": "center", "color": "lime", "fontFamily": "fantasy"}),
                width=12)
    ]),
    html.Hr(),
    html.Br(),
    dbc.Row([
        dbc.Col([
            sidebar
        ], xs=4, sm=4, lg=2, xl=2, xxl=2),
        dbc.Col([
            dash.page_container
        ], xs=8, sm=8, lg=10, xl=10, xxl=10)
    ])
], fluid=True)

if __name__ == "__main__":
    app.run(debug=True)
