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
            html.hr()
#--------sessão de perfil--------#
            dbc.Button(id='botao_avatar',
               children=[html.img(src='/assents/img_hom.png', id='avatar_change', alt='Avatar', className='perfil_name')
                         ])                 
])





# =========  Callbacks  =========== #
# Pop-up receita
