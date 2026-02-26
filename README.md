📊 Análise de Dados – RH

Dataset: IBM HR Analytics


📌 Sobre o Projeto

Este projeto tem como objetivo realizar uma análise completa de dados de Recursos Humanos utilizando o dataset IBM HR Analytics, passando por:

📥 Extração e tratamento dos dados no Python

🔎 Análise Exploratória (EDA)

📊 Criação de métricas estratégicas

📈 Construção de Dashboard no Power BI

🎯 Geração de insights para tomada de decisão

A proposta do projeto é simular um cenário real de consultoria de dados para o setor de RH, com foco em redução de turnover, análise de perfil de colaboradores e apoio estratégico à gestão de pessoas.


🏢 Contexto de Negócio

A área de Recursos Humanos enfrenta desafios como:

Alta taxa de turnover

Baixa retenção de talentos

Falta de visibilidade sobre fatores que influenciam desligamentos

Dificuldade em identificar perfis de risco

Este projeto busca responder perguntas como:

🔹 Qual é a taxa de turnover da empresa?

🔹 Quais departamentos possuem maior índice de desligamento?

🔹 Existe relação entre salário e saída da empresa?

🔹 Funcionários mais jovens pedem mais demissão?

🔹 Tempo de empresa influencia na rotatividade?


🛠️ Tecnologias Utilizadas:

🐍 Python

Pandas


📊 Power BI

📓 Jupyter Notebook

📁 Git & GitHub


🔄 Etapas do Projeto
1️⃣ Importação e Tratamento de Dados (Python)

Leitura do arquivo CSV

Verificação de valores nulos

Padronização de colunas categóricas

Conversão de variáveis (ex: Attrition → binária)

Criação de novas colunas estratégicas:

Faixa etária

Categoria de tempo de empresa

Nível salarial (qcut)

Variáveis auxiliares para análise

2️⃣ Análise Exploratória (EDA)

Principais análises realizadas:

Taxa geral de turnover

Turnover por:

Departamento

Cargo

Faixa etária

Tempo de empresa

Nível salarial

Correlação entre variáveis numéricas

Distribuição de renda

Perfil médio do colaborador que pede demissão

3️⃣ Modelagem para Dashboard

Organização da base para BI

Criação de métricas:

Turnover %

Média salarial

Tempo médio na empresa

Preparação da base para visualização estratégica

4️⃣ Dashboard no Power BI

O dashboard foi construído com foco executivo, contendo:

📌 KPI de Turnover

📌 Turnover por departamento

📌 Turnover por faixa etária

📌 Turnover por tempo de empresa

📌 Distribuição salarial

📌 Filtros dinâmicos

Objetivo: permitir que gestores identifiquem rapidamente áreas críticas e padrões de risco.


📈 Principais Insights Encontrados

(Exemplo – ajustar conforme seus resultados reais)

Funcionários com até 2 anos de empresa possuem maior taxa de saída.

Faixa etária entre 18–35 anos apresenta maior turnover.

Cargos operacionais possuem maior rotatividade.

Nível salarial mais baixo apresenta maior índice de desligamento.


🎯 Impacto para o Negócio

Com base na análise, a empresa poderia:

Criar programas de retenção para novos colaboradores

Rever política salarial para cargos críticos

Desenvolver plano de carreira mais estruturado

Aplicar ações preventivas nos primeiros anos de empresa


📁 Estrutura do Projeto
📦 projeto-ibm-hr-analytics
 ┣ 📂 data
 ┣ 📂 notebooks
 ┣ 📂 dashboard
 ┣ 📜 README.md
 ┗ 📜 requirements.txt


👨🏻‍💻 Autores
Eduardo Farias Oliveira
Rafael de Oliveira Dutra
📍 São Paulo – SP
📊 Foco em Análise de Dados e Business Intelligence
