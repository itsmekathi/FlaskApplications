import dash
import dash_core_components as dcc
import dash_html_components as html
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

def dash_application():
    # Create a Dash application

    dashApp = dash.Dash(
        __name__,
        server=False,
        routes_pathname_prefix='/dash/',
        external_stylesheets=external_stylesheets
    )

    dashApp.layout = html.Div([
        html.H2('Hello World'),
        dcc.Dropdown(
            id='dropdown',
            options=[{'label': i, 'value': i} for i in ['LA', 'NYC', 'MTL']],
            value='LA'
        ),
        html.Div(id='display-value')
    ])

    @dashApp.callback(dash.dependencies.Output('display-value', 'children'),
                    [dash.dependencies.Input('dropdown', 'value')])
    def display_value(value):
        return 'You have selected "{}"'.format(value)

    return dashApp
