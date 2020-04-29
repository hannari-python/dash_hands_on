import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State, MATCH, ALL

app = dash.Dash(__name__, suppress_callback_exceptions=True)

# レイアウト
app.layout = html.Div([
    html.Button("Add Filter", id="add-filter", n_clicks=0),
    html.Div(id='dropdown-container', children=[]),
    html.Div(id='dropdown-container-output')
])

# コールバック
# dropdown-containerにドロップダウンを返す
# childrenにドロップダウンをどんどん加える
# ドロップダウンのidを辞書で作成。"index"の値にボタンのクリック数を渡す
@app.callback(
    Output('dropdown-container', 'children'),
    [Input('add-filter', 'n_clicks')],
    [State('dropdown-container', 'children')])
def display_dropdowns(n_clicks, children):
    new_dropdown = dcc.Dropdown(
        id={
            'type': 'filter-dropdown',
            'index': n_clicks
        },
        options=[{'label': i, 'value': i} for i in ['NYC', 'MTL', 'LA', 'TOKYO']]
    )
    children.append(new_dropdown)
    return children

# インプットにドロップダウン 
# クリックして作られる全てのドロップダウンをALLを用いて指定する
# 全てのドロップダウンの値を使う
# ドロップダウンの全ての値を返すコールバック
@app.callback(
    Output('dropdown-container-output', 'children'),
    [Input({'type': 'filter-dropdown', 'index': ALL}, 'value')]
)
def display_output(values):
    return html.Div([
        html.Div('Dropdown {} = {}'.format(i + 1, value))
        for (i, value) in enumerate(values)
    ])


if __name__ == "__main__":
    app.run_server(debug=True)
