import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mplcursors

data_climat = pd.read_excel("./graph/Climat.xlsx",sheet_name='SI -erreur')
df = pd.DataFrame(data_climat)

# Correction des valeurs en erreur
for month in range(len(df.count())):
    for day in range(len(df.iloc[:, month])):
        if df.iloc[day, month] == "0xFFFF" or df.iloc[day, month] == "Sun":
            df.iloc[day, month] = (df.iloc[day-1, month] + df.iloc[day+1, month])/2

fig, (ax1, ax2) = plt.subplots(2)
names = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre']

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