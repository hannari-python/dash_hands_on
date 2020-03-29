import dash  
import dash_core_components as dcc 
import dash_html_components as html    
import plotly.express as px 
from dash.dependencies import Input, Output 

import json 

gapminder = px.data.gapminder()

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Gapminder Data"),
    dcc.Graph(id="my_graph", figure=px.scatter(gapminder, x="gdpPercap", y="lifeExp", size="pop", log_x=True, log_y=True, color="continent", hover_data=["country"], animation_frame="year", size_max=80)),
    html.H1(id="show_data")
])

@app.callback(Output("show_data", "children"),
            [Input("my_graph", "hoverData")])
def update_data(hoverData):
    if hoverData is None:
        dash.exceptions.PreventUpdate
    else:
        return json.dumps(hoverData["points"][0]["customdata"][0])

if __name__ == "__main__":
    app.run_server(debug=True)