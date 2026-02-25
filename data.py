#%%
import pandas as pd
import json

#Esta pegando o csv no meu local (Eduardo)
df = pd.read_csv(r"C:\Users\eduar\Documents\Estudos\Projeto_IBM\data\data_ibm.csv")

#%%
#analise das colunas
df.info()
df.describe()
df.isnull().sum() #verifica se tem informações nulas

#%%
#Cria coluna de faixa etaria para melhor analise no power bi, alem de melhor entedimento para usuario
df["Faixa-etaria"] = pd.cut(
    df["Age"],
    bins=[18,25,35,45,60],
    labels=["18-25", "26-35", "36-45", "46-60"]
)

df.head(10)

