import dash  
import dash_core_components as dcc 
import dash_html_components as html 
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__) 

df = pd.read_csv('https://www.customs.go.jp/toukei/shinbun/trade-st/timeseries_202005.csv', 
                 header=2, parse_dates=[0], encoding='shift-jis').dropna()
df['balance'] = df['Exp-Total'] - df['Imp-Total']
df['month'] = df['Years/Months'].apply(lambda x: x.month)

selector = ['all'] + [m for m in range(1,13)]

app.layout = html.Div([
    
    html.H1('貿易収支'),
    
    dcc.Dropdown(
        id = 'boueki_dropdown',
        options = [{"label": m, 'value': m} for m in selector],
        value = [4],
        multi=True
    ),
    
    dcc.Graph(
        id = 'boueki_graph_line'
    ),
    dcc.Graph(
        id = 'boueki_graph_bar'
    )
    
    
    
])

@app.callback(
    [Output('boueki_graph_line', 'figure'),
    Output('boueki_graph_bar', 'figure')],
     
     
     [Input('boueki_dropdown', 'value')]
             )
def update_graph(selected_values):
    dff = df[df['month'].isin(selected_values)]

    if 'all' in selected_values:
        return px.line(df, x='Years/Months', y=['Exp-Total', 'Imp-Total']),px.bar(df,x='Years/Months', y='balance')
    
    return px.line(dff, x='Years/Months', y=['Exp-Total', 'Imp-Total']),px.bar(dff,x='Years/Months', y='balance')


app.run_server(debug=True)