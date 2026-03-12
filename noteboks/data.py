#%%
import pandas as pd
import os
import json


# Pega o local onde este script está salvo
base_path = os.path.dirname(os.path.abspath(__file__))

# Define os caminhos de entrada e saída voltando uma pasta para 'data'
input_path = os.path.join(base_path, "..", "data", "data_ibm.csv")
output_path = os.path.join(base_path, "..", "data", "data_ibm_tratado.csv")


try:
    df = pd.read_csv(input_path)
    print("Arquivo carregado com sucesso!")
except FileNotFoundError:
    print(f"ERRO: Arquivo não encontrado em {input_path}")
    exit()

#ANALISE DAS COLUNAS
df.isnull().sum()
df.info()
df.head()

# CRIAÇÃO DE COLUNAS

df["Faixa-etaria"] = pd.cut(
    df["Age"],
    bins=[18,25,35,45,60],
    labels=["18-25", "26-35", "36-45", "46-60"],
    include_lowest=True
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

df["distancia_casa"] = pd.cut(
    df["DistanceFromHome"],
    bins=[0,5,15, float('inf')],
    labels=["Perto (0-5km)", "Médio (6-15km)", "Longe (+15km)"]
)

df["Attrition_num"] = (
    df["Attrition"]
    .astype(str)
    .str.strip()
    .map({"Yes":1, "No":0})
)

# ANALISE EXPLORATORIA

print(f"{df['Attrition_num'].mean() * 100:.2f}%")
print(df.groupby("Faixa-etaria")["Attrition_num"].mean())
print(df.groupby("tempo_empresa")["Attrition_num"].mean())

# EXPORTAÇÃO PARA POWER BI

df.to_csv(output_path, index=False)
print(f"Arquivo tratado exportado com sucesso para: {output_path}")