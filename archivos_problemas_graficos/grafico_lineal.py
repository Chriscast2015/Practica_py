import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivos_problemas_graficos\\p.csv")
print(df)

#creando un plano cartesiano
sns.lineplot(x="fecha", y="p",data = df)

#creando un punto en le maximo
plt.plot("01-07",10,"o")

#mostrando grafico
plt.show()
