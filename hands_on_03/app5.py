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
                template={"layout": {"dragmode": "select"}},
            ),
        ),
        html.H1(id="show_text"),
    ]
)

# hoverData, clickData, selectedData属性
# selectedData属性は
#  "layout": {"clickmode":"event"+select} を指定する必要 / pxの場合 templateに渡す
# "dragmode" : "select" を指定すると、ドラッグで範囲が選択できる


@app.callback(Output("show_text", "children"), [Input("my_graph", "selectedData")])
def update_content(hoverData):
    return json.dumps(hoverData)


if __name__ == "__main__":
    app.run_server(debug=True)
