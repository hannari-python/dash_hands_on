import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from dash.dependencies import Input, Output, State

gapminder = px.data.gapminder()

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.Div(
            [
                dcc.Dropdown(
                    id="select_country",
                    options=[
                        {"value": i, "label": i} for i in gapminder.country.unique()
                    ],
                    value="Japan",
                )
            ],
            style={"width": "50%", "display": "inline-block"},
        ),
        html.Div(
            [
                dcc.Dropdown(
                    id="drop",
                    options=[{"label": i, "value": i} for i in gapminder.columns[3:6]],
                    value="lifeExp",
                )
            ],
            style={"width": "50%", "display": "inline-block"},
        ),
        dcc.Graph(id="my_graph"),
    ]
)


@app.callback(
    Output("my_graph", "figure"),
    [Input("select_country", "value"), Input("drop", "value")],
)
def update_graph(selected_country, selected_value):
    dff = gapminder[gapminder.country == selected_country]
    return px.line(
        dff, x="year", y=selected_value, title=f"{selected_country}の{selected_value}"
    )


if __name__ == "__main__":
    app.run_server(debug=True)
