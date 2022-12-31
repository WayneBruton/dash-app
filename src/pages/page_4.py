import dash
from dash import Dash, dcc, html, callback, Input, Output
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

dash.register_page(__name__, name="Game Sales", title="Pie")

df = pd.read_csv("./vgsales.csv")
# print(df.head())
areas = ["North American Sales", "EU Sales", "Japan Sales", "Other Sales", "World Sales"]

layout = html.Div([
    dbc.Row([
        dbc.Col([
            dcc.Dropdown([x for x in areas], id='genre_choice', persistence=True, value="World Sales"),
        ], xs=10, sm=10, lg=8, xl=4, xxl=4)
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='pie-fig')
        ], width=12)
    ])

]
)


@callback(
    Output('pie-fig', 'figure'),
    Input('genre_choice', 'value')
)
def update_graph(value):
    fig = px.pie(data_frame=df, values=value, names="Genre", color='Genre', title="Video Game sales By region")
    return fig
