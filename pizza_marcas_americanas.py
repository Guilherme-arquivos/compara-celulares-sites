import matplotlib.pyplot as plt
import seaborn as sns 
import pandas as pd

dados =  pd.read_csv("produtos_americanas_marcas.csv")
marc = dados["marca"].value_counts()

plt.pie(
    marc,
    labels=marc.index,
    autopct='%1.2f%%'
)
plt.axis("equal")
plt.title("Proporção das marcas entre os 91 primeiros celulares")
plt.show()