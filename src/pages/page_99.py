import dash
from dash import Dash, dcc, html
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

dash.register_page(__name__, name="About Me", title="About")

layout = html.Div([
    html.P('What I do', style={"fontWeight": "bold", "color": "white"}),
    # html.Br(),
    html.P("My name is Wayne Bruton, After many years as a Financial Manager I decided to learn how to code."
           "I started with Javascript. I have used NodeJS extensively and use MySQL and MongoDB as databases."
           " On the front-end I use VueJs (3) and use Quasar and Vuetify. I recently discovered Python and now "
           "use it extensively in my job too. I work for a property development and investment company and until "
           "recently was the only developer there. We are now a team of two. We have developed a web-based app that "
           "manages the various investment accounts, does daily interest, prints statements & loan agreements to PDF"
           " files and generally manages the investors which amount to over R100 million. We also, within the same app,"
           " monitor and project manage the construction side of the business. Managing subcontractors, "
           "creating payment "
           "advices (as PDF Documents), payment requisitions also as PDF's and the creation of various excel documents"
           " created out of the database using both Javascript and Python. Purchase orders are created in "
           "Xero using the app too. We also have a section dealing with sales of the properties. I am in the "
           "process of creating a dashboard, hence my discovery of Plotly Dash."),
    html.Br(),
    html.P('About me personally', style={"fontWeight": "bold", "color": "white"}),
    # html.Br(),
    html.P('I am 57, I am an avid rugby fan, love reading and mostly just love coding. All I want to do is '
           'code and work remotely'),
    # dcc.Link()
    html.A('LinkedIn Page', href='https://www.linkedin.com/in/wayne-bruton-9a82942b', target='_blank', style={"marginRight": 50}),
    html.A('email', href='mailto:waynebruton@icloud.com', target='_blank')
], style={"margin": "10px 150px"})
