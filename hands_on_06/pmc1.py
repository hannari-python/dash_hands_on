import dash   
import dash_core_components as dcc 
import dash_html_components as html 
from dash.dependencies import Input, Output, State, MATCH 
import plotly.express as px 

gapminder = px.data.gapminder()

comp_style = {"width": "33%", "display": "inline-block"}

app = dash.Dash()

app.layout = html.Div([
    html.Button("Add Tools", id="add_button"),

    html.Div([], id="components_div")
])


@app.callback(Output("components_div", "children"),
    [Input("add_button", "n_clicks")],
    [State("components_div", "children")]
)
def add_components(n_clicks, children):
    if n_clicks is None:
        raise dash.exceptions.PreventUpdate
    new_comps = html.Div([
        dcc.Dropdown(id={"type": "dropdown", "index": n_clicks},
        options=[{"value": i, "label": i} for i in gapminder.country.unique()],
        value = [gapminder.country.unique()[n_clicks]],
        multi=True
        ),
        dcc.Graph(id={"type": "graph", "index": n_clicks})

    ], style = comp_style)

    children.append(new_comps)

    return children

@app.callback(
    Output({"type": "graph", "index": MATCH}, "figure"),
    [Input({"type": "dropdown", "index": MATCH}, "value")]
)
def update_graph(select_values):
    gap = gapminder[gapminder["country"].isin(select_values)]

    return px.line(gap, x="year", y="pop", color="country")

app.run_server(debug=True)

