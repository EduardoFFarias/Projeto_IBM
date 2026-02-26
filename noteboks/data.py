#%%
import pandas as pd
import json

df = pd.read_csv(r"data\data_ibm.csv")

#%% ANALISE DAS COLUNAS
df.isnull().sum()
df.info()
df.head()

#%% CRIAÇÃO DE COLUNAS

df["Faixa-etaria"] = pd.cut(
    df["Age"],
    bins=[18,25,35,45,60],
    labels=["18-25", "26-35", "36-45", "46-60"]
)

df["nivel_salario"] = pd.qcut(
    df["MonthlyIncome"],
    q=3,
    labels=["Baixo", "Médio", "Alto"]
)

df["tempo_empresa"] = pd.cut(
    df["YearsAtCompany"],
    bins=[0,2,5,10,40],
    labels=["0-2 anos", "3-5 anos", "6-10 anos", "10+ anos"],
    include_lowest=True
)

df["Attrition_num"] = (
    df["Attrition"]
    .astype(str)
    .str.strip()
    .map({"Yes":1, "No":0})
)

#%% ANALISE EXPLORATORIA

print(f"{df['Attrition_num'].mean() * 100:.2f}%")
print(df.groupby("Faixa-etaria")["Attrition_num"].mean())
print(df.groupby("tempo_empresa")["Attrition_num"].mean())

#%% EXPORTAÇÃO PARA POWER BI

df.to_csv("data/data_ibm_tratado.csv", index=False)