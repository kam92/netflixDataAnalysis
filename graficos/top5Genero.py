import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dados = pd.read_csv("dataset/netflix_titles.csv", parse_dates=True)
dados.shape

#Filmes
top_filmes = dados.loc[dados["type"] == "Movie"]["listed_in"].value_counts()[:5]
top_filmes_df = top_filmes.reset_index()
top_filmes_df.columns = ["genre", "count"]
plt.figure(figsize=(25, 5))
sns.barplot(x=top_filmes_df["genre"], y=top_filmes_df["count"])
plt.title("Gêneros Mais Populares de Filmes")
plt.show()

#Series
top_shows = dados.loc[dados["type"] == "TV Show"]["listed_in"].value_counts()[:5]
top_shows_df = top_shows.reset_index()
top_shows_df.columns = ["genre", "count"]
plt.figure(figsize=(25, 5))
sns.barplot(x=top_shows_df["genre"], y=top_shows_df["count"])
plt.title("Gêneros Mais Populares de Séries e Shows")
plt.show()
