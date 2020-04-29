import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px

gapminder = px.data.gapminder()  # サンプルデータの読み込み

app = dash.Dash(__name__)  # Dashのインスタンスを作成する

app.layout = html.Div(
    [
        # タイトルの作成
        html.H1("Hello Dash"),
        # グラフの作成
        dcc.Graph(
            figure=px.scatter(
                gapminder,
                x="gdpPercap",
                y="lifeExp",
                size="pop",
                color="continent",
                log_x=True,
            )
        ),
    ]
)

app.run_server(debug=True)
