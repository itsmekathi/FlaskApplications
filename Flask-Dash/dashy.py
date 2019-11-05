import os
from app import create_app

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# server = Flask(__name__)

# @server.route('/')
# def index():
#     return 'Hello Flask app'

# @server.route('/dashboard')
# def dashboard():
#     return render_template('dashboard.iframe.html', title='Dashboard')


# dashApp = dash.Dash(
#     __name__,
#     server=server,
#     routes_pathname_prefix='/dash/',
#     external_stylesheets=external_stylesheets
# )

# dashApp.layout = html.Div([
#     html.H2('Hello World'),
#     html.H3('Welcome onboard'),
#     dcc.Dropdown(
#         id='dropdown',
#         options=[{'label': i, 'value': i} for i in ['LA', 'NYC', 'MTL']],
#         value='LA'
#     ),
#     html.Div(id='display-value')
# ])

# @dashApp.callback(dash.dependencies.Output('display-value', 'children'),
#               [dash.dependencies.Input('dropdown', 'value')])
# def display_value(value):
#     return 'You have selected "{}"'.format(value)