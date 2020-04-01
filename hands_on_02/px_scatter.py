import plotly.express as px  

gapmider = px.data.gapminder()

fig = px.scatter(gapminder, x=[1,2,3,4], y=[3,4,5,6])

fig.show()

