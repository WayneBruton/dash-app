import dash
from dash import Dash, dcc, html, callback, Input, Output, State
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate

dash.register_page(__name__, name="Life Expectancy (2)", title="map")

layout = html.Div([
    dcc.Graph(id='the_graph'),

    html.Div([
        dbc.Input(id="input_state", type='number', inputMode='numeric', value=1952, max=2007, min=1952, step=5,
                  required=True, style={'width':100, "textAlign": "center"}),
        dbc.Button(id='submit_button', n_clicks=0, children='submit'),
        html.Div(id="output_state")
    ], style={"textAlign": "center"})

]
)


@callback(
    [Output("output_state", 'children'),
     Output('the_graph', 'figure')],
    [Input('submit_button', 'n_clicks')],
    [Input("input_state", 'value')]
)
def update_output(n_clicks, val_selected):
    if val_selected is None:
        raise PreventUpdate
    else:
        df = px.data.gapminder()
        df = df[df.year == val_selected]
        fig = px.choropleth(df, locations='iso_alpha', color='lifeExp', hover_name='country',
                            title=f"Life Expectancy - {val_selected}", projection='natural earth',
                            color_continuous_scale=px.colors.sequential.Plasma)
        fig.update_layout(title=dict(font=dict(size=28), x=0.5, xanchor='center'), margin=dict(l=60, r=60, t=50, b=50))
        return f"The input value was {val_selected}, the button has been clicked {n_clicks} times.", fig
