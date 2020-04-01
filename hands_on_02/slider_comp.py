import dash   
import dash_core_components as dcc  

app = dash.Dash(__name__)

app.layout = dcc.Slider()

app.run_server(debug=True)

