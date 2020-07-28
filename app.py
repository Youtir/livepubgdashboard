import dash
import dash_core_components as dcc
import dash_html_components as html
from dash_bootstrap_components import Tooltip
from dash.dependencies import Input, Output
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import datetime
import json
from sqlalchemy.engine import create_engine
import random


ENGINE = create_engine('druid://192.168.178.50:8888/druid/v2/sql/')
external_stylesheets = ['https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css']
external_js = ['https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js']
app = dash.Dash(__name__, external_scripts=external_js, external_stylesheets=external_stylesheets)
app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>My Dashboard</title>
        {%favicon%}
        {%css%}
        <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''
app.layout = html.Div(
    children=[
        html.H2(
            children='Pubg test'
        ),
        html.P(
            children=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            id='datestring'
        ),
        dcc.Interval(
            id='date_update',
            interval=5*1000,
            n_intervals=0
        ),
        html.Div(
            children=[
                html.Div(
                    id='resulttable',
                    children=[],
                    className='col s6'
                )
            ],
            className='row'
        ),
        html.Div(
            children=[],
            id='vis'
        )
    ]
)


def make_table(dataframe):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns]),
            className='white-text teal lighten-2'
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(len(dataframe))
        ], className='teal lighten-4')
    ], className='striped')


def makeCell(rownum, colnum, colour, tooltiptext):
    if colnum==0:
        cname = 'col s1 offset-s1'
    else:
        cname = 'col s1'
    ans = html.Div(
        children=[
            html.I(
                'accessibility',
                className=f'medium material-icons {colour}-text',
                id=f'r{rownum}c{colnum}'
            ),
            Tooltip(
                tooltiptext,
                target=f'r{rownum}c{colnum}'
            )
        ],
        className=cname
    )
    return ans



@app.callback(
    [Output('datestring', 'children'),
    Output('vis', 'children')],
    [Input('date_update', 'n_intervals')]
)
def update_time(n):
    query = """
    SELECT
        "character.name"
        , "character.teamId"
        , LATEST("elapsedTime") etime
        , LATEST("character.health") lhealth
    FROM
        "pubg"
    GROUP BY
        "character.name"
        , "character.teamId"
    ORDER BY
        "character.teamId"
    """
    df = pd.read_sql(query, ENGINE)
    rows = []
    count = 0
    for j in range(10):
        cols = []
        for i in range(10):
            health = df.iloc[count]['lhealth']
            if health == 0:
                colour = 'black'
            elif 0 < health <= 25:
                colour = 'red'
            elif 25 < health <= 75:
                colour = 'yellow'
            else:
                colour = 'green'
            tooltip = f"Name: {df.iloc[count]['character.name']}, Health: {df.iloc[count]['lhealth']}, Team: {df.iloc[count]['character.teamId']}"
            cols.append(makeCell(j, i, colour, tooltip))
            count+=1
        rows.append(
            html.Div(
                className='row',
                children=cols
            )
        )
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), rows


if __name__ == "__main__":
    app.run_server(debug=True, host='0.0.0.0')


# with t1 as (
# SELECT
#     "character.name"
#     , "character.teamId"
#     , LATEST("elapsedTime") etime
#     , LATEST("character.health") lhealth
# FROM
#     "pubg"
# GROUP BY
#     "character.name"
#     , "character.teamId"
# ORDER BY
#     "character.teamId"
# )
# SELECT
#     "character.teamId"
#     , avg(lhealth) avghealth
# FROM
#     t1
# GROUP BY
#   "character.teamId"
# ORDER BY
#   "character.teamId"