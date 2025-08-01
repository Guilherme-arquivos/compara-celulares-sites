import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

dados = pd.read_csv("produtos_americanas_marcas.csv")
sns.boxplot(
    data=dados,
    y="preço",
    color="orange",
    showmeans=True,
    showfliers=True
)
plt.title("Boxplot dos preços dos celulares")
plt.ylabel("Preços")
plt.show()