import dash   
import dash_core_components as dcc   
import dash_html_components as html  
import plotly.express as px  

from dash.dependencies import Input, Output, State

graph_list = [px.line, px.scatter, px.bar]

app = dash.Dash(__name__)

app.layout = html.Div([

    dcc.Dropdown(
        id='mydropdown',
        options=[{'label': f'{type.__name__}', 'value': num} for num, type in enumerate(graph_list)],
        value = 0
    ),

    
    html.Button(
        id='mybutton',
        children="PUSHME"
    ),


    dcc.Graph(
        id='mygraph'
    )

])

@app.callback(
    Output('mygraph', 'figure'),
    [Input('mybutton', 'n_clicks')],
    [State('mydropdown', 'value')]
)
def update_graph(n_clicks, selected_value):
    return graph_list[selected_value](
        x=[1,2,3,4,5],
        y=[1,2,3,4,5]
    )

if __name__ == '__main__':
    app.run_server(debug=True)
