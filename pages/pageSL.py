from dash import html, register_page

register_page(__name__, path='/sl', name='pageSL')

layout = html.Div([

    html.P('Home page')


])