import dash
from dash import dcc, html, Input, Output, callback
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

# META TAGS TITLE / IMAGE / DESCRIPTION
dash.register_page(__name__, name='Life Expectancy', title='Histogram', image='page_1.png',
                   description='An Awesome App')

# Page 1 Data
df = px.data.gapminder()
# print(df.head())

layout = html.Div([
    dbc.Row([
        dbc.Col([
            dcc.Dropdown([x for x in df.continent.unique()], id='cont_choice', persistence=True),
        ], xs=10, sm=10, lg=8, xl=4, xxl=4)
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='line-fig')
        ], width=12)
    ])

]
)


@callback(
    Output('line-fig', 'figure'),
    Input('cont_choice', 'value')
)
def update_graph(value):
    if value is None:
        fig = px.histogram(df, x='continent', y='lifeExp', histfunc='avg', color='continent', title="Life Expectancy "                                                                                                  "by Continent")
    else:
        dff = df[df.continent == value]
        fig = px.histogram(dff, x='country', y='lifeExp', histfunc='avg', color='country',
                           title=f"Life Expectancy - {value}")
    return fig
