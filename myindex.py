from dash import html, dcc
import dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

import app

from components import sidebar, dashboards, extratos


# =========  Layout  =========== #
content = html.Div(id="page-content")


app.layout = dbc.Container(children=[
  dbc.row([
        dbc.Col([dcc.Location(id="url"),
            sidebar.layout
        ], md=2, style={'background-color': 'red', 'height': '100vh'}),
    dbc.Col([
        content
    ], md=10, style={'backgroud-color': 'blue', 'height': '100vh'})
])
]
, fluid=True,)
@app.callback(Output('page-content','children'), [input('url', 'pathname')])
def render_page(pathname):
    if pathname == '/' or pathname == '/dashboards':
        return dashboards.layout

    if pathname == '/extratos':
        return extratos.layout


if __name__ == '__main__':
    app.rum_server(port=5500, debug=True)

