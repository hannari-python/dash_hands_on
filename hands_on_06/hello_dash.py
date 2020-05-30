import dash   
import dash_html_components as html  

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.H1("HEllo DaSh!", style={"backgroundColor": "orange", "height": "300px", "width": "300px", "boxShadow": "10px 10px 5px 0 rgb(0, 0, 0)"})

app.run_server(debug=True)
