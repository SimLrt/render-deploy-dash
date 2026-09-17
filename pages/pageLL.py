from dash import html, register_page

register_page(__name__, path='/ll', name='pageLL')

layout = html.Div([

    html.P('Home page')

])