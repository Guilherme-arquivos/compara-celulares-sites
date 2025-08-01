# Compara Celulares - Scraping e Análise de Preços
Este projeto realiza web scraping dos sites da Americanas e Casas Bahia para coletar dados sobre as ofertas dos celulares disponíveis. A partir desses dados são feitas análises comparativas, com a geração de gráficos, sobre os preços e a frequência das marcas nos dois sites.

## Objetivo
Além de analisar os preços, o projeto também busca entender quais marcas possuem maior destaque nas primeiras páginas dos sites. Isso porque a primeira página é a parte mais visitada por usuários antes de tomarem uma decisão de compra, sendo então muito influente nas decisões dos consumidores.
Ao focar nos primeiros 20 celulares exibidos por cada site, o projeto busca evidenciar a concentração da exposição em torno das marcas mais populares.
O site das Casas Bahia apresenta entre os primeiros 20 resultados apenas celulares das marcas samsung e motorola, enquanto que o site da Americanas apresenta 15 celulares pertencentes a essas marcas. As análises comparativas utilizam os primeiros 20 celulares pertencentes a essas duas marcas.

## Tecnologias Utilizadas
- Python
- Playwright - para realizar o scraping das páginas
- Pandas - para tratamento e análise dos dados
- SQLite3 - para unir e consultar dados entre as tabelas
- Matplotlib e Seaborn - para criação de gráficos

## Funcionalidades
### Etapas do Projeto:
1. **Coleta de dados**
- Coleta os primeiros 20 celulares do site das Casas Bahia e os 91 do site da Americanas, utilizando playwright.
- Salva os dados em duas tabelas, uma para cada site, por meio do uso de pandas.
2. **Tratamento dos dados**
- Um script adiciona a coluna "marca" nas tabelas, usando pandas.
3. **Comparação entre os preços médios**
- Um script junta as tabelas com os dados da Casas Bahia e os 20 primeiros celulares da Samsung ou Motorola da Americanas.
- Esse programa calcula e compara os preços médios por marca entre os dois sites, utilizando sqlite3 e pandas.
- Outro script faz um gráfico de barras comparando o preço por marca, utilizando pandas, matplotlib e seaborn.
4. **Comparação entre as frequências das marcas**
- Sabendo que os primeiros 20 celulares da Casas Bahia são ou da Samsung ou da Motorola, esse script compara a frequência das marcas a qual os consumidores são expostos entre os primeiros 20 desse site e os primeiros 20 das mesmas marcas da Americanas.
- Gera gráficos para ilustrar essa distribuição de visibilidadde.
5. **Análise aprofundada dos dados da Americanas**
  - Cria:
    - Gráfico de pizza com a proporção das marcas.
    - Gráfico de dispersão com os preços individuais.
    - Boxplot com distribuição de preços.

## Organização dos arquivos
- celulares_comparacoes.py - coleta os dados da Casas Bahia e da Americanas.
- identificador_marcas_americanas.py - adiciona a coluna "marca" aos produtos da Americanas.
- identificador_marcas_casasbahia.py - adiciona a coluna "marca" aos produtos da Casas Bahia.
- comparativo_marcas_sites_media.py - compara os preços médios das marcas nos dois sites.
- comparativo_marcas_sites_total.py - compara a frequência das marcas nos dois sites.
- media_precos_grafico_comparacao.py - forma o gráfico de barras comparando o preço médio.
- total_precos_grafico_comparacao.py - forma o gráfico de barras comparando a frequência das marcas.
- pizza_marcas_americanas.py - forma o gráfico de pizza com a proporção das  marcas entre os celulares da Americanas.
- dispersao_precos_americanas.py - forma o gráfico de dispersão de preços da Americanas.
- boxplot_precos_americanas.py - forma o boxplot dos preços da Americanas.
- Tabelas ".csv" e Gráficos ".png" estão disponíveis no repositório 

## Como executar
- Tenha Python instalado.
- Instale as dependências.
