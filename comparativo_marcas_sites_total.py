import sqlite3
import pandas as pd

conexao = sqlite3.connect("banco.db")
dados_americanas = pd.read_csv("produtos_americanas_marcas.csv")
dados_casasbahia = pd.read_csv("produtos_casasbahia_marcas.csv")
dados_americanas.to_sql("americanas", conexao, if_exists="replace", index=False)
dados_casasbahia.to_sql("casasbahia", conexao, if_exists="replace", index=False)

consulta = """
    SELECT loja, marca, COUNT(preço) AS quantidade_total 
    FROM (
        SELECT  * FROM(
            SELECT marca, preço, loja FROM americanas WHERE marca IN ('samsung', 'motorola') LIMIT 20
        ) AS a
        UNION ALL
        SELECT * FROM(
            SELECT marca, preço, loja FROM casasbahia LIMIT 20
        ) AS b
    )
    WHERE marca IN ('samsung', 'motorola')
    GROUP BY loja, marca
"""
resultado = pd.read_sql_query(consulta, conexao)    
resultado.to_csv("comparacao_total.csv", index=False, encoding="utf-8")

conexao.close()