import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

df = pd.read_csv("data\melt_zaisei.csv", index_col=0)

col_selector = df.columns[:-1]

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        dcc.Dropdown(
            id="mydropdown",
            options=[{"label": c, "value": c} for c in col_selector],
            value=["main_title", "variable", "title"],
            multi=True,
            clearable=False,
        ),
        dcc.Graph(id="mytree"),
        dcc.Graph(id="mysun", style={"height": 800}),
    ]
)


@app.callback(Output("mytree", "figure"), [Input("mydropdown", "value")])
def make_tree(selected_values):
    return px.treemap(df, path=selected_values, values="value")


@app.callback(Output("mysun", "figure"), [Input("mydropdown", "value")])
def make_tree(selected_values):
    return px.sunburst(df, path=selected_values, values="value")


if __name__ == "__main__":
    app.run_server(debug=True)
