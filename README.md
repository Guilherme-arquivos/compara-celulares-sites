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
- Coleta os primeiros 20 celulares do site das Casas Bahia e os 91 do site da Americanas.
- Salva os dados em duas tabelas, uma para cada site.
2. **Tratamento dos dados**
- Um script adiciona a coluna "marca" nas tabelas.
3. **Comparação entre sites**
- Outro script junta as tabelas com os dados da Casas Bahia e os 20 primeiros celulares da Samsung ou Motorola da Americanas.
- Esse script calcula e compara os preços médios por marca entre os dois sites, utilizando sqlite3 e pandas. 
