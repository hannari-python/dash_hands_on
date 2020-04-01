import dash  
import dash_html_components as html 
import dash_core_components as dcc    

import pandas as pd 
import plotly.express as px   

df = pd.read_excel("../data/covid-world-data.xls")

countries = ["Japan", "Austria"]
dff = df[df["CountryExp"].isin(countries)]

app = dash.Dash(__name__)

app.layout = html.Div([
    
    dcc.Dropdown(
        id="myCallback",
        options=[{"value": i, "label": i} for i in df.CountryExp.unique()],
        value=["Japan", "Austria"],
        multi=True,
    ),
    
    
    dcc.Graph(
        id="myGraph",
        
    )
])


@app.callback(
    dash.dependencies.Output("myGraph", "figure"),
    [dash.dependencies.Input("myCallback", "value")]
)
def update_graph(select_value):
    dff = df[df["CountryExp"].isin(select_value)]
    return px.line(dff, x="DateRep", y="NewConfCases", color="CountryExp")

app.run_server(debug=True)