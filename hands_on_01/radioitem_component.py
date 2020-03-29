import dash   
import dash_core_components as dcc  

app = dash.Dash(__name__)

app.layout = dcc.RadioItems(
   options=[
       {"label": "test", "value": "test"},
       {"label": "test2", "value": "test2"},
       {"label": "test3", "value": "test3"}
   ]
)

app.run_server(debug=True)


