import dash  
import dash_daq as daq   

app = dash.Dash(__name__)

app.layout = daq.Thermometer(
    value=80,min=-10, max=100, height=300
)

app.run_server(debug=True)