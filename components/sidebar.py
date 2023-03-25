import os
import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from app import app

from datetime import datetime, date
import plotly.express as px
import numpy as np
import pandas as pd


# ========= Layout ========= #
layout = dbc.Col([
            html.h1("myBudget", className="text-primary"),
            html.p("By ASIMOV", className="text-info"),
            html.hr(),
#--------sessão de perfil--------#
            dbc.Button(id='botao_avatar',
               children=[html.img(src='/assents/img_hom.png', id='avatar_change', alt='Avatar', className='perfil_avatar')
                         ], style={'backgraou-color':'transparent', 'border-color': 'trasnparent' }),                 
#--------sessão novo--------#
            dbc.row([
               dbc.col([
                  dbc.Button(color='success', id='opne-novo-receita',
                             children=['+ Receita'])
               ],width=6),
               dbc.col([
                  dbc.Button(color='danger', id='opne-novo-despesa',
                             children=['+ Despesa'])
               ])
            ]),
#--------sessão NAV--------#
            html.hr(),
            dbc.Nav(
               [
                  dbc.NavLink("Dashboard", href="/dashboards", active="exact"),
                  dbc.NavLink("Extratos", href="/extratos", active="exact"),
               ], vertical=True, pills=True, id='nav_buttons', style={"margin-buttom": "50px"}),
],id='sidebar_completa')


# =========  Callbacks  =========== #
# Pop-up receita
