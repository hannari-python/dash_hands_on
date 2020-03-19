import dash  
import dash_core_components as dcc 
import dash_html_components as html    
import plotly.express as px 
from dash.dependencies import Input, Output 

import os 
import json 

gapminder = px.data.gapminder()

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Gapminder Data"),
    dcc.Graph(id="my_graph", figure=px.scatter(gapminder, x="gdpPercap", y="lifeExp", size="pop", log_x=True, log_y=True, color="continent", hover_data=["country"], animation_frame="year", size_max=80, template={"layout":{"clickmode": "event+select"}})),
    dcc.Graph(id="show_data")
])

@app.callback(Output("show_data", "figure"),
            [Input("my_graph", "selectedData")])
def update_data(hoverData):
    if hoverData is None:
        jp_gap = gapminder[gapminder.country.isin(["Japan"])]
        return px.line(jp_gap, x="year", y="gdpPercap", hover_data=["country"],title="Japan")
    else:
        cont_list = []
        for i in hoverData["points"]:
            cont_list.append(i["customdata"][0])
        c_gap = gapminder[gapminder.country.isin(cont_list)]

        return px.line(c_gap, x="year", y="gdpPercap", color="country", hover_data=["country"])

if __name__ == "__main__":
    app.run_server(debug=True)