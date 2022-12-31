import dash
from dash import dcc, html, Input, Output, callback
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

dash.register_page(__name__, name="Tipping Chart", title="Tips")

# Page 1 Data
df = px.data.tips()

layout = html.Div([
    dbc.Row([
        dbc.Col([
            html.Img(src="/assets/smoking.jpg")
            # html.Img(src="smoking.jpeg")
        ], width=4),
        dbc.Col([
            dcc.RadioItems([x for x in df.day.unique()], id='day-choice', value='Sun'),
        ], width=8)
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='bar-fig', figure=px.bar(df, x='smoker', y='total_bill', color='sex'))

        ], width=12)
    ])
])


@callback(
    Output('bar-fig', 'figure'),
    Input('day-choice', 'value')
)
def update_graph(value):
    # print(value)
    dff = df[df.day == value]
    fig = px.bar(dff, x='smoker', y='total_bill', color='sex')
    return fig
