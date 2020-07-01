import dash   
import dash_core_components as dcc   
import dash_html_components as html  
import plotly.express as px 

from dash.dependencies import Input, Output 


gapminder = px.data.gapminder()

app = dash.Dash()

app.layout = html.Div([

    dcc.Dropdown(id='dropdown',
        options=[{'label': c, 'value': c} for c in gapminder.country.unique()],
        value = 'Japan'
    
    
    ),
    dcc.Graph(id='graph')


    ])
@app.callback(
    Output('graph', 'figure'),
    [Input('dropdown', 'value')]
)
def update_graph(selected_value):
    gap = gapminder[gapminder['country'] == selected_value]
    return px.scatter(gap, x='year', y='gdpPercap')

app.run_server(debug=True)


