import dash   
import dash_core_components as dcc  
import dash_html_components as html  
import plotly.express as px  

import os 

gap = px.data.gapminder()

app = dash.Dash(__name__)

server = app.server  

app.layout = html.Div([
    html.H1("ヘロクへのデプロイ", style={"textAlign":"center"}),
    dcc.Graph(
        figure=px.scatter(
            gap,
            x="gdpPercap",
            y="lifeExp",
            size="pop",
            color="continent",
            size_max=70,
            animation_frame="year",
            log_x=True,
            range_y=[20, 90]
        )
    )
])

if __name__ == "__main__":
    app.run_server(debug=True)
