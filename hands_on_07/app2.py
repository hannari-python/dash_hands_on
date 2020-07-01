import dash   
import dash_core_components as dcc 
import dash_html_components as html 
import pandas as pd
import plotly.express as px

from dash.dependencies import Input, Output

df = pd.read_csv('https://www.customs.go.jp/toukei/shinbun/trade-st/timeseries_202005.csv', header=2, parse_dates=['Years/Months']).dropna()
df['balance'] = df['Exp-Total'] - df['Imp-Total']
df['month'] = df['Years/Months'].apply(lambda x: x.month)

app = dash.Dash(__name__)


app.layout = html.Div([
    
    html.H1('輸出入'),
    
    dcc.Dropdown(
        id='mydropdown',
        options = [{'value': m, 'label': m} for m in df['month'].unique()],
        value=[5],
        multi=True
    ),
    
    dcc.Graph(id='mygraph'),
    
    dcc.Graph(id='mygraph2'),
    
    
])
@app.callback(
    [Output('mygraph', 'figure'),
     Output('mygraph2', 'figure')],
    [Input('mydropdown', 'value')]
)
def update_graph(selected_value):
    dff = df[df['month'].isin(selected_value)]
    return px.line(dff, x='Years/Months', y=['Exp-Total', 'Imp-Total']), px.bar(dff, x='Years/Months', y='balance')


app.run_server(debug=True) 

