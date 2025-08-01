import pandas as pd

dados = pd.read_csv("dados_produtos_americanas.csv")

marcas = {
    "samsung": ["samsung"],
    "motorola": ["motorola"],
    "xiaomi": ["xiaomi"],
    "infinix": ["infinix"],
    "positivo": ["positivo"],
    "realme": ["realme"],
}
def parte_numero(preço):
    numero = preço[2:-3]
    sem_ponto = numero.replace('.', '')
    return float(sem_ponto)
    
def identificar_marca(modelo):
    modelo = modelo.lower()
    for marca, palavras in marcas.items():
        for palavra in palavras:
            if palavra in modelo:
                return marca
    return "marcas menores"
    
dados["marca"] = dados["modelo"].apply(identificar_marca)
dados["preço"] = dados["preço"].apply(parte_numero)
dados.to_csv("produtos_americanas_marcas.csv", index=False, encoding="utf-8")    