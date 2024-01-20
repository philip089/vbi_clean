import dash
from dash import html
from pyvis.network import Network
import networkx as nx
import dash_bootstrap_components as dbc



app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CERULEAN])

app.layout = html.Div(children=[
    html.H1(children='Yotube Hashtags'),

    ##############  Pyvis html graph import  #####################
    html.Div(children=[
        html.Iframe(src="assets/tag_network.html",
                    style={"height": "1067px", "width": "100%"})
    ])
])
if __name__ == "__main__":
    app.run_server()
