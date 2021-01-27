import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mplcursors

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
print(min_max)

#Courbe pour chaque mois et annuel
month_filter = 0
liste = []
for month in range(len(df.count())-1):
    plt.suptitle(names[month_filter])
    month_filter = month_filter+1
    plt.xlabel('Jours')
    plt.ylabel('Température (°C)')
    plt.plot(df.iloc[:, month_filter])
    mplcursors.cursor()
    plt.show()
    for day in range(len(df.iloc[:, month_filter])):
        plt.xlabel('Jours de l\'année')
        plt.ylabel('Température (°C)')
        liste.append(df.iloc[day, month_filter])
plt.plot(liste)
mplcursors.cursor()
plt.show()
    
# Année
# plt.xlabel('Jours')
# plt.ylabel('Température (°C)')
# plt.plot(df.iloc[:, 1:13])
# plt.show()