import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

venda_gasolina = pd.read_csv('gasolina.csv')

with sns.axes_style('whitegrid'):
 grafico=sns.lineplot(data=venda_gasolina, x="dia", y="venda", color="red")
 grafico.set_title("Valor da Gasolina")
 plt.show(grafico)
 plt.savefig('venda_gasolina.png')