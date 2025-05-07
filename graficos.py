import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('C:/Users/pimen/Downloads/ecommerce_preparados.csv')
print(df.head())
print(df.info())
print(df.describe())
print(df.columns)

sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

# Histograma das notas dos produtos
plt.figure()
sns.histplot(df['Nota'], bins=20, kde=True, color='skyblue')
plt.title('Distribuição das Notas dos Produtos')
plt.xlabel('Nota')
plt.ylabel('Frequência')
plt.grid(True)

# Gráfico de dispersão entre preço e número de avaliações
plt.figure()
sns.scatterplot(x='N_Avaliações', y='Preço_MinMax', data=df, hue='Nota', palette='viridis')
plt.title('Dispersão entre Avaliações e Preço (Normalizado)')
plt.xlabel('Número de Avaliações')
plt.ylabel('Preço (Normalizado)')
plt.legend(title='Nota')

# Mapa de calor de correlação
plt.figure()
corr = df[['Nota', 'N_Avaliações', 'Desconto', 'Preço_MinMax', 'Marca_Freq', 'Material_Freq']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Mapa de Calor das Correlações')

# Gráfico de barras das marcas mais comuns
plt.figure()
top_marcas = df['Marca'].value_counts().nlargest(10)
sns.barplot(x=top_marcas.values, y=top_marcas.index, hue=top_marcas.index, palette='crest')
plt.title('Top 10 Marcas com Mais Produtos')
plt.xlabel('Quantidade de Produtos')
plt.ylabel('Marca')

# Gráfico de pizza de gêneros dos produtos
plt.figure()
genero_counts = df['Gênero'].value_counts()
plt.pie(genero_counts, labels=genero_counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette("pastel"))
plt.title('Distribuição de Gênero dos Produtos')

# Gráfico de densidade
plt.figure()
sns.kdeplot(df['Preço_MinMax'], fill=True, color='green')
plt.title('Densidade dos Preços dos Produtos (Normalizado)')
plt.xlabel('Preço (Normalizado)')
plt.ylabel('Densidade')

# Gráfico de regressão entre nota e número de avaliações
plt.figure()
sns.regplot(x='N_Avaliações', y='Nota', data=df, scatter_kws={'alpha':0.5}, line_kws={"color": "red"})
plt.title('Relação entre Número de Avaliações e Nota')
plt.xlabel('Número de Avaliações')
plt.ylabel('Nota')

plt.tight_layout()
plt.show()