from datetime import datetime 

import dash  
import dash_core_components as dcc   

app = dash.Dash()

app.layout = dcc.DatePickerRange(
    display_format="YYYY MM DD",
    start_date = datetime(2020, 3,19),
    end_date = datetime(2020, 6, 3),
    calendar_orientation = "vertical"
)

app.run_server(debug=True)

