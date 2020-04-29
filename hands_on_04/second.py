import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from dash.dependencies import Input, Output, State

# gapminderデータから日本のものだけ選択する
gapminder = px.data.gapminder()
gap_jp = gapminder[gapminder["country"] == "Japan"]

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        # 人口、平均余命、1人当たりGDPを選択できる
        # ドロップダウンの作成
        dcc.Dropdown(
            id="drop",
            options=[{"label": i, "value": i} for i in gapminder.columns[3:6]],
            value="lifeExp",
        ),
        # コールバックで作成したグラフを描画する
        # コンポーネント
        dcc.Graph(id="my_graph"),
    ]
)

# コールバックの作成
@app.callback(Output("my_graph", "figure"), [Input("drop", "value")])
# コールバック関数
def update_graph(selected_value):
    return px.line(gap_jp, x="year", y=selected_value, title=f"日本の{selected_value}")


if __name__ == "__main__":
    app.run_server(debug=True)
