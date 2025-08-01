import matplotlib.pyplot as plt
import seaborn as sns 
import pandas as pd

dados = pd.read_csv("comparacao_total.csv")
sns.barplot(
    data=dados,
    x="marca",
    y="quantidade_total",
    estimator=sum,
    hue="loja",
    palette={"americanas":"red", "casas bahia":"blue"}
)
plt.title("Quantidade de celulares por marca nas primeiras 20 ofertas")
plt.xlabel("Marca do celular")
plt.ylabel("Quantidade de celulares")
plt.show()