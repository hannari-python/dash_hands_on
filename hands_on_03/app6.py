import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from dash.dependencies import Input, Output, State
import json

gapminder = px.data.gapminder()

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        dcc.Graph(
            id="my_graph",
            figure=px.scatter(
                gapminder,
                x="gdpPercap",
                y="lifeExp",
                size="pop",
                animation_frame="year",
                log_x=True,
                range_y=[20, 90],
                color="continent",
                size_max=70,
                hover_data=["country"],
            ),
        ),
        dcc.Graph(id="show_figure1", style={"width": "33%", "display": "inline-block"}),
        dcc.Graph(id="show_figure2", style={"width": "33%", "display": "inline-block"}),
        dcc.Graph(id="show_figure3", style={"width": "33%", "display": "inline-block"}),
    ]
)

# hoverData, clickData, selectedData属性
# selectedData属性は
#  "layout": {"clickmode":"event"+select} を指定する必要 / pxの場合 templateに渡す
# "dragmode" : "select" を指定すると、ドラッグで範囲が選択できる


@app.callback(
    [
        Output("show_figure1", "figure"),
        Output("show_figure2", "figure"),
        Output("show_figure3", "figure"),
    ],
    [Input("my_graph", "hoverData")],
)
def update_content(hoverData):
    if hoverData is None:
        raise dash.exceptions.PreventUpdate
    country = hoverData["points"][0]["customdata"][0]
    sele_data = gapminder[gapminder.country == country]
    return (px.line(sele_data, x="year", y="pop", title=f"{country}の人口データ"),
    px.line(sele_data, x="year", y="gdpPercap", title=f"{country}の1人当たりGDPデータ"),
    px.line(sele_data, x="year", y="lifeExp", title=f"{country}の平均余命データ"))


if __name__ == "__main__":
    app.run_server(debug=True)
