import pandas as pd
import plotly.graph_objects as go

dados = pd.read_csv("dataset/netflix_titles.csv", parse_dates=True)
dados.shape

top_paises = dados.country.value_counts()
top_paises = top_paises[:30][::-1]
trace = go.Bar(x=top_paises.values,
               y=top_paises[:30].index, orientation='h', name='', marker=dict(color='#6ad49b'))
layout = go.Layout(title="Quantidade de títulos produzidos por país",
                   height=700, legend=dict(x=0.1, y=1.1))
fig = go.Figure([trace], layout=layout)
fig.show()
