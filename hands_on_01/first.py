import dash  
import dash_core_components as dcc  
import dash_html_components as html 
from dash.dependencies import Input, Output 

import plotly.express as px  

# データの読み込み
gapminder = px.data.gapminder()
gapminder2007 = gapminder[gapminder["year"]==2007]
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
    figure=px.scatter(gapminder2007, x="gdpPercap", y="lifeExp", size="pop", color="continent", log_x=True)
    )

])

if __name__ == "__main__":
    app.run_server(debug=True, host='0.0.0.0')

