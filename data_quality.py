import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tabulate import tabulate

class DataQuality:
    def __init__(self, df):
        self.df = pd.read_csv(df)

    def info_df(self):
        print("Informações gerais:")
        print(self.df.info())
        print("\n")    

    def contar_nulos(self):
        print("Quantidade de valores nulos por coluna:")
        conta_nulos = self.df.isnull().sum().reset_index()
        conta_nulos.columns = ["Colunas", "Valores"]
        print(tabulate(conta_nulos, headers='keys', tablefmt='fancy_grid'))
        print("\n")

    def contar_valores_unicos(self):
        print("Quantidade de valores únicos por coluna:")
        valores_unicos = self.df.nunique().reset_index()
        valores_unicos.columns = ["Colunas", "Valores"]
        print(tabulate(valores_unicos, headers='keys', tablefmt='fancy_grid'))
        print("\n")

    def value_counts_categ(self):
        print("Análise das colunas categóricas:")
        colunas_categoricas = self.df.select_dtypes(include=['object', 'category'])
        nomes_colunas_cat = colunas_categoricas.columns.to_list()
        print(f"Colunas a serem analisadas: {nomes_colunas_cat}")


        for col in colunas_categoricas.columns:
            value_counts = self.df[col].value_counts().reset_index()
            value_counts.columns = [col, "Frequência"]
            print(f"\nDistribuição de valores na coluna {col}:")
            print(tabulate(value_counts, headers='keys', tablefmt='fancy_grid'))
        print("\n")

    def descricao_numerica(self):
        print("Descrição estatística das colunas numéricas:")
        colunas_numericas = self.df.select_dtypes(include=['int64', 'float64'])
        print(tabulate(colunas_numericas.describe(), headers='keys', tablefmt='fancy_grid'))
        print("\n")

    def plot_distribuicao_categorica(self):
        print("Distribuições das colunas categóricas:")
        colunas_categoricas = self.df.select_dtypes(include=['object', 'category'])
        for col in colunas_categoricas.columns:
            plt.figure(figsize=(20, 5))
            sns.countplot(y=self.df[col], order=self.df[col].value_counts().index, palette="viridis", legend=False)
            plt.title(f'Distribuição de {col}')
            plt.show()

    def plot_distribuicao_numerica(self):
        print("Distribuições das colunas numéricas:")
        colunas_numericas = self.df.select_dtypes(include=['int64', 'float64'])
        for col in colunas_numericas.columns:
            plt.figure(figsize=(20, 5))
            sns.histplot(self.df[col], kde=True, bins=30, color='blue')
            plt.title(f'Distribuição de {col}')
            plt.show()

    def matriz_correlacao(self):
        colunas_numericas = self.df.select_dtypes(include=['int64', 'float64'])
        correlacao = colunas_numericas.corr()

        plt.figure(figsize=(10, 6))
        sns.heatmap(correlacao, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
        plt.title('Matriz de Correlação')
        plt.show()
        print("\n")

    def plot_outliers(self):
        print("Outliers:")
        numeric_cols = self.df.select_dtypes(include=['int64', 'float64'])
        for col in numeric_cols.columns:
            plt.figure(figsize=(8, 4))
            sns.boxplot(x=self.df[col])
            plt.title(f'Outliers em {col}')
            plt.show()
        print("\n")

    def temporal_analysis(self):
        datetime_cols = self.df.select_dtypes(include=['datetime64[ns]'])
        for col in datetime_cols.columns:
            self.df.set_index(col).resample('M').size().plot()
            plt.title(f'Frequência ao longo do tempo em {col}')
            plt.show()
        print("\n")

    def generate_report(self):
        print("Iniciando análise de qualidade de dados...\n")
        print("Aqui estão as 3 primeiras e as 3 últimas linhas do DataFrame:")
        print(tabulate(self.df.head(3), headers='keys', tablefmt='fancy_grid'))
        print("\n")
        print(tabulate(self.df.tail(3), headers='keys', tablefmt='fancy_grid'))
        print("\n")

        # Informações gerais
        self.info_df()
        
        # Contagem de valores nulos
        self.contar_nulos()
        
        # Contagem de valores únicos
        self.contar_valores_unicos()
        
        # value_counts das colunas categóricas
        self.value_counts_categ()

        # Gráficos de distribuição
        self.plot_distribuicao_categorica()
        
        # Describe das colunas numéricas
        self.descricao_numerica()

        # Gráficos de distribuição
        self.plot_distribuicao_numerica()

        # Correlação entre matrizes
        self.matriz_correlacao()

        # Dados que se afastam significativamente da maioria e podem distorcer a análise
        self.plot_outliers()

        # Análise temporal (se tiver colunas de datas)
        self.temporal_analysis()

        print("Relatório concluído.")