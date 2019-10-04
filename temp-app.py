import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input

from influxdb import InfluxDBClient


def get_last_temp():
    """Return the last temperature measurement"""
    client = InfluxDBClient(host='localhost', port=8086)
    client.switch_database('indaba_session')
    query = 'select last("Temperature") from "Indaba Session"'

    result = client.query(query)

    result_list = list(result.get_points())
    return result_list[0]['last']


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Current Temperature'),

    html.Div([
        dcc.Dropdown(
            id='param-select',
            options=[
                {'label': 'Temperature', 'value': 'TMP'}
            ],
            value='TMP'
        ),
        html.H5(id='temp',
                children='24°C',
                style={
                    'textAlign': 'center'
                }),
    ], className='row two columns'),
])


@app.callback(
    Output('temp', 'children'),
    [Input('param-select', 'value')]
)
def format_current_temp(param):

    return str(get_last_temp()) + '°C'

if __name__ == '__main__':
    app.run_server(debug=True)
