# Projeto DataQuality
Projeto de análise genérica de dados.

## Proposta:
Crie seu dataquality Utilizando de POO, crie um módulo que importado para um jupyter notebook crie um relatório como no pandas-profiling/YData-profiling/SweetViz. Neste módulo, tera um método geral para análise de qualquer dataset:

- Contagem de nulos
- Contagem de valores únicos
- value_counts em colunas categóricas
- describe nas colunas numéricas
- gráficos de distribuição de colunas categóricas
- gráficos de distribuição de colunas numéricas

## Como utilizar:
`from data_quality import DataQuality as dq`

`df = dq.generate_report()`

### Análises feitas além do proposto:
- Matriz de correlação entre dados numéricos
- Outliers
- Análise temporal (se tiver um campo data)
