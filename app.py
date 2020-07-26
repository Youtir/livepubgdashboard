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


engine = create_engine('druid://192.168.178.50:8888/druid/v2/sql/')
colors = ['green-text', 'red-text']
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
            interval=10*1000,
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
            className='row',
            children=[
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text tooltipped',
                            id='r1c1',
                            **{"data-position": "bottom"},
                            **{"data-tooltip": "I am a tooltip"}
                        )
                    ],
                    className='col s1 offset-s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text',
                            id='r1c2',
                            **{"data-position": "bottom"},
                            **{"data-tooltip": "I am a tooltip"}
                        ),
                        Tooltip(
                            "This is a tooltip",
                            target='r1c2'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                )
            ]
        ),
        html.Div(
            className='row',
            children=[
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1 offset-s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                )
            ]
        ),
        html.Div(
            className='row',
            children=[
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1 offset-s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                )
            ]
        ),
        html.Div(
            className='row',
            children=[
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1 offset-s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                )
            ]
        ),
        html.Div(
            className='row',
            children=[
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1 offset-s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                )
            ]
        ),
        html.Div(
            className='row',
            children=[
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1 offset-s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                )
            ]
        ),
        html.Div(
            className='row',
            children=[
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1 offset-s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                )
            ]
        ),
        html.Div(
            className='row',
            children=[
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1 offset-s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                )
            ]
        ),
        html.Div(
            className='row',
            children=[
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1 offset-s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                )
            ]
        ),
        html.Div(
            className='row',
            children=[
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1 offset-s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                ),
                html.Div(
                    children=[
                        html.I(
                            'accessibility',
                            className='medium material-icons green-text'
                        )
                    ],
                    className='col s1'
                )
            ]
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



@app.callback(
    # Output('datestring', 'children'),
    # # Output('resulttable', 'children')],
    # [Input('date_update', 'n_intervals')]
    [Output('datestring', 'children'),
    Output('r1c1', 'className')],
    [Input('date_update', 'n_intervals')]
)
def update_time(n):
    # query = """
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
    # """
    # df = pd.read_sql(query, engine)
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 'medium material-icons '+random.choice(colors)


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