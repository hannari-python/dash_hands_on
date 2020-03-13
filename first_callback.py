import dash  
import dash_core_components as dcc  
import dash_html_components as html 
from dash.dependencies import Input, Output 

import plotly.express as px  

# データの読み込み
gapminder = px.data.gapminder()
gapminder2007 = gapminder[gapminder.year=="2007"]
# Dashインスタンスの作成
app = dash.Dash(__name__)

# レイアウトの作成
app.layout = html.Div([

    html.H1("Gapminder"),

    dcc.Dropdown(id="first-dropdown", 
        options=[{"value": i, "label": i} for i in gapminder.country.unique()],
        value="Japan"
    ),
    dcc.Graph(id="select_graph",
    )

])

# コールバックの作成
@app.callback(Output("select_graph", "figure"),
            [Input("first-dropdown", "value")])
def update_graph(selected_value):
    dff = gapminder[gapminder["country"]==selected_value]
    return px.line(dff, x="year", y="pop")

if __name__ == "__main__":
    app.run_server(debug=True)
