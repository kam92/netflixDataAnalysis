import plotly.graph_objects as go
import pandas as pd

dados = pd.read_csv("dataset/netflix_titles.csv", parse_dates=True)
dados.shape

grupos_netflix = dados.type.value_counts()
trace = go.Pie(labels=grupos_netflix.index, values=grupos_netflix.values, pull=[0.05])
layout = go.Layout(title="Porcentagem total de Séries e Filmes", height=500, legend=dict(x=1.1, y=1.3))
fig = go.Figure(data=[trace], layout=layout)
fig.update_layout(height=500, width=700)
fig.show()
