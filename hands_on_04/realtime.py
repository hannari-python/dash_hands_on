from datetime import datetime, timedelta 

import dash  
import dash_core_components as dcc 
import dash_html_components as html  
import pandas as pd 

import plotly.express as px 

from dash.dependencies import Input, Output 

df = pd.read_csv("./data/df_realtime_update.csv", index_col=0)

app = dash.Dash(__name__)

app.layout = html.Div([

    html.H1("リアルタイム更新"),

    dcc.Interval(
        id="update_tool",
    ),

    dcc.Graph(
        id="realtime_graph"
    )

])

@app.callback(Output("realtime_graph", "figure"),
            [Input("update_tool", "n_intervals")]
)
def update_graph(n_intervals):

    now_time = datetime.now()
    m_time = now_time - timedelta(seconds=120)
    
    now_time = now_time.time().isoformat(timespec="seconds")
    m_time = m_time.time().isoformat(timespec="seconds")

    dff = df.loc[m_time: now_time]
    
    return px.line(x=dff.index, y=dff["price"])

app.run_server(debug=True)


