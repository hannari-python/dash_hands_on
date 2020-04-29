import dash  
import dash_core_components as dcc  
import dash_html_components as html  
from dash.dependencies import Input, Output, State, MATCH, ALL


app = dash.Dash(__name__, suppress_callback_exceptions=True)

app.layout = html.Div([
    html.Button("Add Filter", id="dynamic-add-filter", n_clicks=0),
    html.Div(id="dynamic-dropdown-container", children=[])
])

@app.callback(Output("dynamic-dropdown-container", "children"),
            [Input("dynamic-add-filter", "n_clicks")],
            [State("dynamic-dropdown-container", "children")]
            )
def display_dropdown(n_clicks, children):
    new_element = html.Div([
        dcc.Dropdown(
            id={"type": "dynamic-dropdown", "index": n_clicks},
            options=[{"label": i, "value": i} for i in ["京都", "東京", "大阪"]]
        ),
        html.Div(
            id={"type":"dynamic-output", "index": n_clicks}
        )
    ])
    children.append(new_element)
    return children

@app.callback(
    Output({"type": "dynamic-output", "index": MATCH}, "children"),
    [Input({"type": "dynamic-dropdown", "index": MATCH}, "value")],
    [State({"type": "dynamic-dropdown", "index": MATCH}, "id")]
)
def display_value(value, id):
    return html.Div(f"Dropdown {id['index']}= {value}")

app.run_server(debug=True)
