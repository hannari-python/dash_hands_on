import dash   
import dash_html_components as html 
import dash_core_components as dcc  
import plotly.express as px  

from datetime import datetime 

iris = px.data.iris()

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("HEllo DaSh!"),
    dcc.DatePickerRange(
    display_format="YYYY MM DD",
    start_date = datetime(2020, 3,19),
    end_date = datetime(2020, 6, 3),
    calendar_orientation = "vertical"
    ),
    dcc.Graph(
    figure=px.scatter(iris, x="sepal_width", y="sepal_length", color="species")
)
])

app.run_server(debug=True)
