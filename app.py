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

gameid = 'match.bro.official.2018-06.oc.squad-fpp.2018.06.17.2bb9faed-9ddb-4d07-be1c-6a7a4244d1e6' # 'match.bro.official.2018-06.oc.squad-fpp.2018.06.13.f564defe-21e2-4d01-bbf6-08ab62e6de92' #
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
                    children=[
                        html.Div(
                            children=[],
                            id='vis'
                        )
                    ],
                    className='col s4'
                ),
                html.Div(
                    id='killtable',
                    className='col s4'
                ),
                html.Div(
                    children=[
                        dcc.Graph(
                            id='mapplot',
                            config={'displayModeBar': False}
                        )
                    ],
                    className='col s4'
                )
            ],
            className='row'
        )
        # html.Div(
        #     children=[],
        #     id='vis'
        # )
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
    # if colnum==0:
    #     cname = 'col s1 offset-s1'
    # else:
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

def makeCell2(rownum, colnum, colour, tooltiptext):
    ansI = html.I(
        'accessibility',
        className=f'medium material-icons {colour}-text',
        id=f'r{rownum}c{colnum}'
    )
    ansT = Tooltip(
        tooltiptext,
        target=f'r{rownum}c{colnum}'
    )
    return ansI, ansT


@app.callback(
    [Output('datestring', 'children'),
    Output('vis', 'children'),
    Output('killtable', 'children'),
    Output('mapplot', 'figure')],
    [Input('date_update', 'n_intervals')]
)
def update_time(n):
    query = f"""
    SELECT
        "character.name"
        , "character.teamId"
        , LATEST("elapsedTime") etime
        , LATEST("character.health") lhealth
        , MAX("__time") ltime
        , LATEST("character.location.x") x
        , LATEST("character.location.y") y
    FROM
        "pubg"
    WHERE
        "common.matchId" = '{gameid}'
    GROUP BY
        "character.name"
        , "character.teamId"
    ORDER BY
        "character.teamId"
    """
    df = pd.read_sql(query, ENGINE)
    query2 = f"""
    select
        "killer.name" AS "Player"
        , count(*) AS "Kills"
    from
        "pubg-kill-log"
    WHERE
        __time < '{df['ltime'].max()}'
        AND "common.matchId" = '{gameid}'
    GROUP BY
        "killer.name"
    ORDER BY
        "Kills" desc
    """
    df2 = pd.read_sql(query2, ENGINE)
    df2 = df2.iloc[:10]
    # df = pd.read_csv('sample.csv')
    # df = df.iloc[:50]
    rows = []
    count = 0
    ok = True
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
            # a, t = makeCell2(j, i, colour, tooltip)
            # cols.append(a)
            # cols.append(t)
            count+=1
            if count == len(df):
                ok = False
                break
        rows.append(
            html.Div(
                className='row',
                children=cols
            )
        )
        if not ok:
            break
    fig = go.Figure(data=go.Scatter(
        x=df['x'],
        y=df['y'],
        mode='markers',
        marker_color=df['character.teamId'],
        text=df['character.name'],
    ))
    fig.update_layout(
        autosize=False,
        width=800,
        height=800
    )
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), rows, make_table(df2), fig


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