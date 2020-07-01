import dash   
import dash_core_components as dcc   
import dash_html_components as html 
import pandas as pd 
import plotly.express as px 
from dash.dependencies import Input, Output, State, MATCH  

df = pd.read_csv('data\zaisei_detail.csv', index_col=0)
df = df.melt(id_vars=['main_title', 'title'])


col_selector = df.columns[:-1]
app = dash.Dash(__name__)

app.layout = html.Div([
    
    dcc.Dropdown(
        id='mydropdown',
        options=[{'label': i, 'value': i} for i in col_selector],
        value=['main_title', 'title', 'variable'],
        multi=True
    ),
    dcc.Graph(id='mytree'),
    dcc.Graph(id='mysun')


])


@app.callback(
    Output('mytree', 'figure'),
    [Input('mydropdown', 'value')]
)
def tree(selected_values):
    return px.treemap(df, path=selected_values, values='value')

@app.callback(
    Output('mysun', 'figure'),
    [Input('mydropdown', 'value')]
)
def sunbu(selected_values):
    return px.sunburst(df, path=selected_values, values='value')

app.run_server(debug=True)


