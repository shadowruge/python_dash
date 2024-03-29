from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_excel('data_project.xlsx')

app = Dash(__name__)



if __name__ == '__main__':
    app.run(debug=True)
