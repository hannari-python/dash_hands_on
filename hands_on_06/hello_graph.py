import dash  
import dash_core_components as dcc  
import plotly.express as px  

iris = px.data.iris()

app = dash.Dash(__name__)

app.layout = dcc.Graph(
    figure=px.scatter(iris, x="sepal_width", y="sepal_length", color="species")
)

app.run_server(debug=True)
