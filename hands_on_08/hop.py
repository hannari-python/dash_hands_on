import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

graph_list = [px.line, px.scatter, px.bar]

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        dcc.Dropdown(
            options=[
                {"label": f"{type.__name__}", "value": num}
                for num, type in enumerate(graph_list)
            ],
            value=0,
        ),
        html.Button("PUSHME"),
        dcc.Graph(),
    ]
)


if __name__ == "__main__":
    app.run_server(debug=True)
