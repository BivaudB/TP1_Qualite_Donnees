import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data_climat = pd.read_excel("./graph/Climat.xlsx",sheet_name='SI ')
df = pd.DataFrame(data_climat)

#Moyenne
average = df.mean(axis=0,skipna = True)
names = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Aout', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
plt.bar(names,average)
plt.suptitle('Moyenne des mois')
plt.show()

#Ecart-type
ecart_type = df.std(axis=0,skipna=True)
plt.bar(names,ecart_type)
plt.suptitle('Ecart-type des mois')
plt.show()

#Min et Max
min_max = df.agg(["min","max"])
