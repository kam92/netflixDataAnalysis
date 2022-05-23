import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dados = pd.read_csv("dataset/netflix_titles.csv", parse_dates=True)
dados.shape

plt.figure(figsize=(30, 30))
sns.countplot(y="release_year", data=dados, hue="type")
plt.title("Quantidade de Filmes e Séries por Ano de Lançamento")
plt.show()