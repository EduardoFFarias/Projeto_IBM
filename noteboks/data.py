#%%
import pandas as pd
import json

df = pd.read_csv(r"..\data\data_ibm.csv")
#%%
#========================#
# ANALISE DAS COLUNAS #
#========================#

df.isnull().sum() #verifica se tem informações nulas
df.info()
df.head()
#%%
#=====================================================#
# CRIAÇÃO DE COLUNAS PARA MELHOR ANALISE NO POWER BI #
#=====================================================#

#Cria coluna de faixa etaria para melhor analise no power bi, alem de melhor entedimento para usuario
df["Faixa-etaria"] = pd.cut(
    df["Age"],
    bins=[18,25,35,45,60],
    labels=["18-25", "26-35", "36-45", "46-60"]
)

#Cria coluna de divisao por faixa salarial
df["nivel_salario"] = pd.qcut(
            df["MonthlyIncome"],
            q=3,
            labels = ["Baixo", "Médio", "Alto"]
)


#Cria coluna de divisao por tempo de empresa
df["tempo_empresa"] = pd.cut(
    df["YearsAtCompany"],
    bins=[0,2,5,10,40],
    labels=["0-2 anos", "3-5 anos", "6-10 anos", "10+ anos"],
    include_lowest=True
)

df.head()

#Cria coluna de demitidos de forma numerica (sim:1, nao:0), para melhor analise exploratoria
df["Attrition_num"] = (
    df["Attrition"]
    .astype(str)
    .str.strip()
    .map({"Yes":1, "No":0})
)
df.head()
#%%
#============================
# ANALISE EXPLORATORIA #
#============================
#Taxa geral turnouver
print(f"{df["Attrition_num"].mean() * 100:2f}%")

#Turnouver por faixa-etaria
print(df.groupby("Faixa-etaria")["Attrition_num"].mean())

#Turnouver por tempo de empresa
print(df.groupby("tempo_empresa")["Attrition_num"].mean())
