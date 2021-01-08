import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data_climat = pd.read_excel("./graph/Climat.xlsx",sheet_name='SI ')
df = pd.DataFrame(data_climat)

fig, (ax1, ax2) = plt.subplots(2)
names = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Aout', 'Septembre', 'Octobre', 'Novembre', 'Décembre']

#Moyenne
average = df.mean(axis=0,skipna = True)
ax1.bar(names,average)
ax1.set_title('Moyenne des mois')

#Ecart-type
ecart_type = df.std(axis=0,skipna=True)
ax2.bar(names,ecart_type)
ax2.set_title('Ecart-type des mois')
plt.show()

#Min et Max
min_max = df.agg(["min","max"])

#Courbe pour chaque mois
month_filter = 0
for month in range(len(df.count())):
    month_filter = month_filter+1
    plt.suptitle(names[month])
    plt.xlabel('Jours de ')
    plt.ylabel('Température (°C)')
    print(df.iloc[:, month_filter])
    plt.plot(df.iloc[:, month_filter])
    plt.show()