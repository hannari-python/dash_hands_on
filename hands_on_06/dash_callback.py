import dash   
import dash_core_components as dcc  
import dash_html_components as html 
import plotly.express as px 

from dash.dependencies import Input, Output 

gapminder = px.data.gapminder()

graph_style = {"width": "33%", "display": "inline-block"}

app = dash.Dash()


app.layout = html.Div([
    
    html.Div([
        dcc.Dropdown(
            id="dropdown",
            options = [{"label": i, "value": i} for i in gapminder.country.unique()],
            value=["Japan"],
            multi=True
        )
    ]),

    html.Div([
        dcc.Graph(id="graph1", style=graph_style),
        dcc.Graph(id="graph2", style=graph_style),
        dcc.Graph(id="graph3", style=graph_style),

    ]),

], style={"padding": "3%"})

@app.callback(
    [Output("graph1", "figure"),
    Output("graph2", "figure"),
    Output("graph3", "figure"),
    ],
    
    
    [Input("dropdown", "value")]
)
def update_graph(dropdown_value):
    if dropdown_value is None:
        raise dash.exception.PreventUpdate
    gap = gapminder[gapminder["country"].isin(dropdown_value)]
    pop_graph = px.line(gap, x="year", y="pop", color="country", title="population")
    life_graph = px.line(gap, x="year", y="lifeExp", color="country", title="life expectation")
    gdp_graph = px.line(gap, x="year", y="gdpPercap", color="country", title="GDP per Cap")
    return pop_graph, life_graph, gdp_graph



app.run_server(debug=True)
