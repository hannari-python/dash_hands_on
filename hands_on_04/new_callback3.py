import dash   
import dash_core_components as dcc   
import dash_html_components as html  
from dash.dependencies import Input, Output, State, MATCH, ALL, ALLSMALLER
import pandas as pd   
import plotly.express as px  

gapminder = px.data.gapminder()
df = gapminder[gapminder.year == 2007]

app = dash.Dash(__name__, suppress_callback_exceptions=True)

app.layout = html.Div([
    html.Button('Add Filter', id='add-filter-ex3', n_clicks=0),
    html.Div(id='container-ex3', children=[]),
])

# コールバック1
# ボタンクリックでドロップダウンをcontainder-ex3に追加する
# ドロップダウンの下にコールバック2からのデータを得る
# ドロップダウン、Divともにidの"index"にボタンのn_clicks属性を取る
@app.callback(
    Output('container-ex3', 'children'),
    [Input('add-filter-ex3', 'n_clicks')],
    [State('container-ex3', 'children')])
def display_dropdowns(n_clicks, existing_children):
    existing_children.append(html.Div([
        dcc.Dropdown(
            id={
                'type': 'filter-dropdown-ex3',
                'index': n_clicks
            },
            options=[{'label': i, 'value': i} for i in df['country'].unique()],
            # ドロップダウンの初期値をクリック回数で選択
            value=df['country'].unique()[n_clicks]
        ),
        html.Div(id={
            'type': 'output-ex3',
            'index': n_clicks
        })
    ]))
    return existing_children

# コールバック2
# ドロップダウンの選択値をMATCHとALLSMALLERセレクタの両方を利用
# 出力先はid名output-ex3のindexがマッチしているコンポーネント
# 
@app.callback(
    Output({'type': 'output-ex3', 'index': MATCH}, 'children'),
    [Input({'type': 'filter-dropdown-ex3', 'index': MATCH}, 'value'),
     Input({'type': 'filter-dropdown-ex3', 'index': ALLSMALLER}, 'value')],
)
def display_output(matching_value, previous_values):

    # 選択された
    all_values = [matching_value] + previous_values[::-1]
    dff = df[df["country"].isin(all_values)]
    avg_lifexp = dff['lifeExp'].mean()

    # Return a slightly different string depending on number of values
    if len(all_values) == 1:
        return html.Div(f'{avg_lifexp:.2f} is the life expectancy of {matching_value}')
    elif len(all_values) == 2:
        return html.Div(f'{avg_lifexp:.2f} is the average life expectancy of {" and ".join(all_values)}')
    else:
        return html.Div(f'{avg_lifexp:.2f} is the average life expectancy of {" and ".join(all_values[:-1])}, and {all_values[-1]}')

if __name__ == '__main__':
    app.run_server(debug=True)

    