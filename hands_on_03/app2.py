import dash
import dash_html_components as html
import dash_core_components as dcc

from dash.dependencies import Input, Output, State

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# テキストエリアへの入力をH1コンポーネントに出力するアプリ

app.layout = html.Div(
    [
        dcc.Textarea(id="textarea", style={"height": 300, "width": 800}),
        html.Button(id="my_button", n_clicks=0, children="おす"),
        html.H1(id="text_output"),
    ]
)


@app.callback(
    Output("text_output", "children"),
    [Input("my_button", "n_clicks")],
    [State("textarea", "value")],
)
def update_text(n_clicks, textarea_value):
    return textarea_value


if __name__ == "__main__":
    app.run_server(debug=True)
