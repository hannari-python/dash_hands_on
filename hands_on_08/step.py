import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from dash.dependencies import MATCH, Input, Output, State

graph_list = [px.line, px.scatter, px.bar]

gapminder = px.data.gapminder()

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        ### CALLBACK
        dcc.Dropdown(
            id="mydropdown",
            options=[
                {"label": f"{type.__name__}", "value": num}
                for num, type in enumerate(graph_list)
            ],
            value=0,
        ),
        html.Button(id="mybutton", children="PUSHME"),
        dcc.Graph(id="mygraph"),
        ##### PATTERN MATCHING CALLBACK
        html.Button(id="mybutton2", children="ADDME"),
        html.Div(id="pmc", children=[]),
    ],
    style={"padding": "3%"},
)

### CALLBACK


@app.callback(
    Output("mygraph", "figure"),
    [Input("mybutton", "n_clicks")],
    [State("mydropdown", "value")],
)
def update_graph(n_clicks, selected_value):
    return graph_list[selected_value](x=[1, 2, 3, 4, 5], y=[1, 2, 3, 4, 5])


### PATTERN MATCHING CALLBACK


@app.callback(
    Output("pmc", "children"),
    [Input("mybutton2", "n_clicks")],
    [State("pmc", "children")],
    prevent_initial_call=True,
)
def update_layout(n_clicks, exist_children):

    add_layout = html.Div(
        [
            dcc.Dropdown(
                id={"type": "pmcdropdown", "id": n_clicks},
                options=[{"value": c, "label": c} for c in gapminder.country.unique()],
                value=gapminder.country.unique()[n_clicks],
            ),
            dcc.Graph(id={"type": "pmcgraph", "id": n_clicks}),
        ]
    )
    exist_children.append(add_layout)
    return exist_children


@app.callback(
    Output({"type": "pmcgraph", "id": MATCH}, "figure"),
    [Input({"type": "pmcdropdown", "id": MATCH}, "value")],
)
def update_match_graph(selected_value):
    gap = gapminder[gapminder.country == selected_value]
    return px.scatter(
        gap,
        x="gdpPercap",
        y="lifeExp",
        size="pop",
        animation_frame="year",
        range_x=[gap.gdpPercap.min() * 0.8, gap.gdpPercap.max() * 1.2],
        range_y=[gap.lifeExp.min() * 0.8, gap.lifeExp.max() * 1.2],
    )


if __name__ == "__main__":
    app.run_server(debug=True)
