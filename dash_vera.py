import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
folium_map = 'https://cartografiacolaborativa.000webhostapp.com/flask_app.html'

sidebar = html.Div(
    [
        html.H2("Menu de seleção", className="display-4", style={'font-size': '30px', 'font-weight': 'bold'}),
        html.Hr(style={"border-top": "1px solid black", }),
        html.P(
            "Escolha uma opção para visualizar", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Mapa", href="/page-1", id="page-1-link"),
                dbc.NavLink("O que é Cartografia Colaborativa?", href="/page-2", id="page-2-link"),
                dbc.NavLink("Sobre", href="/page-3", id="page-3-link"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style={
        "position": "fixed",
        "top": 0,
        "left": 0,
        "bottom": 0,
        "width": "20%",
        "background-color": "#ffffff"
    },
)
content = html.Div(id="page-content", style={
    "background": None,
    "height": "100%",
    "width": "80%",
    "position": "absolute",
    "top": 0,
    "right": 0,
    "background-color": "#f5f5f5"
})
app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


@app.callback(
    [Output(f"page-{i}-link", "active") for i in range(1, 4)],
    [Input("url", "pathname")],
)
def toggle_active_links(pathname):
    if pathname == "/":
        return True, False, False
    return [pathname == f"/page-{i}" for i in range(1, 4)]


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname in ["/", "/page-1"]:
        return html.P(html.Iframe(src=folium_map, style={"height": "100%", "width": "100%", "position": "absolute", "top": 0, "right": 0}))
    elif pathname == "/page-2":
        return html.P("put a text about Cartography")  # POSSIBILIY OF PUT TEXT FROM GITHUB (TXT)
    elif pathname == "/page-3":
        return html.P("Oh cool, this is page 3!")  # INFORMATION ABOUT CONSTRUCTION

    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised...")
        ]
    )


if __name__ == "__main__":
    app.run_server(debug=True)
