import dash  
import dash_html_components as html  

app =dash.Dash()

app.layout = html.P("Hello Hanpy!")

app.run_server(debug=True)

