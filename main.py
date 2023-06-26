from dash import Dash, html, dash_table
import plotly.express as px
import pandas as pd
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Output, Input


# Carrega os dados do Excel usando o Pandas
df = pd.read_excel("data_project.xlsx")

# Obtém todos os nomes únicos
nomes_unicos = ['Todos os nomes'] + sorted(df.nome.unique())

# Inicializa o app Dash
app = Dash(__name__)

app.layout = html.Div([
    html.H1("View Analysis Statistcs"),
    dash_table.DataTable(data=df.to_dict('records'), page_size=6),
    dcc.Dropdown(
        id='nome',
        options=[{'label': x, 'value': x} for x in nomes_unicos],
        value='Todos os nomes'
    ),
    dcc.Graph(id='my-graph', figure={})
])


@app.callback(
    Output(component_id='my-graph', component_property='figure'),
    Input(component_id='nome', component_property='value')
)
def interactive_graphing(value_nome):
    if value_nome == 'Todos os nomes':
        dff = df
    else:
        dff = df[df.nome == value_nome]
    
    fig = px.bar(data_frame=dff, x='produto', y='valor')
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
