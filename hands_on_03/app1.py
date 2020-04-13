import dash
import dash_html_components as html
import dash_core_components as dcc

from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# テキストエリアへの入力をH1コンポーネントに出力するアプリ

app.layout = html.Div([dcc.Textarea(id="textarea"), html.H1(id="text_output")])


@app.callback(Output("text_output", "children"), [Input("textarea", "value")])
def update_text(textarea_value):
    return textarea_value


if __name__ == "__main__":
    app.run_server(debug=True)
