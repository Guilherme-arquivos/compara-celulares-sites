from playwright.sync_api import sync_playwright
import pandas as pd

def mais_produtos(pagina):
    try:
        if pagina.locator("text='ver mais produtos'").is_visible():
            pagina.click("text='ver mais produtos'")
    except:        
        return False

urls = [
    "https://www.americanas.com.br/s?q=smartphones&sort=score_desc&page=0",
    "https://www.casasbahia.com.br/celulares/b"
]
url_base_americanas = "https://www.americanas.com.br"
    
with sync_playwright() as p:
    
    for l in range(len(urls)):
        
        modelos = []
        preços = []
        loja = []

        navegador = p.chromium.launch(headless=False)
        pagina = navegador.new_page()
        pagina.goto(urls[l])
        pagina.wait_for_timeout(8000)
        pagina.mouse.wheel(0, 2000)
        pagina.wait_for_timeout(1000)
        
        if l == 0:
            celulares = pagina.locator("div.ProductCard_productCard__MwY4X")
            mais_produtos(pagina)
            mais_produtos(pagina)
            mais_produtos(pagina)
            mais_produtos(pagina)
            for i in range(120):
                celular = celulares.nth(i)
                modelo = celular.locator("h3.ProductCard_productName__mwx7Y").text_content().strip()
                preço = celular.locator("span.ProductCard_discountPrice__Q2BeA").first.text_content().strip()
                if modelo and preço:
                    loja.append("americanas")
                    modelos.append(modelo)
                    preços.append(preço)    
            dados = pd.DataFrame({
                "modelo": modelos,
                "preço": preços,
                "loja": loja
            })    
            dados.to_csv("dados_produtos_americanas.csv", index=False, encoding="utf-8")
        
        elif l == 1:
            celulares = pagina.locator("div.styles__ProductCardWrapper-sc-af9a9e0d-3.styles__ResponsiveWrapper-sc-af9a9e0d-6.gawMSK.jzxeQF")
            for i in range(20):
                celular = celulares.nth(i)
                modelo = celular.locator("h3.product-card__title").text_content().strip()
                preço = celular.locator("span.product-card__discount-text").first.text_content().strip()
                if modelo and preço:
                    loja.append("casas bahia")
                    modelos.append(modelo)
                    preços.append(preço)
            dados = pd.DataFrame({
                "modelo": modelos,
                "preço": preços,
                "loja": loja
            })    
            dados.to_csv("dados_produtos_casasbahia.csv", index=False, encoding="utf-8")
            
        navegador.close()