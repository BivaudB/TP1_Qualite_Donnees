import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mplcursors

data_climat = pd.read_excel("./graph/Climat.xlsx",sheet_name='SI ',index_col=0)
df = pd.DataFrame(data_climat)


fig, (ax1, ax2) = plt.subplots(2)
names = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Aout', 'Septembre', 'Octobre', 'Novembre', 'Décembre']

#Moyenne
average = df.mean(axis=0,skipna = True)
ax1.bar(names,average)
ax1.set_title('Moyenne des mois')

#Ecart-type
st_deviation = df.std(axis=0,skipna=True)
ax2.bar(names,st_deviation)
ax2.set_title('Ecart-type des mois')
plt.show()

#Min et Max
min = df.min()
max = df.max()
plt.plot(min,color="blue",label='Minimum')
plt.plot(max,color="red",label='Maximum')
plt.xlabel('Mois')
plt.ylabel('Température (°C)')
plt.title("Minimum et maximum")
legend = plt.legend(loc='lower right', shadow=True, fontsize='x-large')
legend.get_frame().set_facecolor('C0')
plt.show()

#Courbe pour chaque mois et annuel
month_filter = 0
liste = []
for month in range(len(df.count())):
    plt.suptitle(names[month_filter])
    plt.xlabel('Jours')
    plt.ylabel('Température (°C)')
    plt.plot(df.iloc[:, month_filter])
    mplcursors.cursor()
    plt.show()
    month_filter += 1
    for day in range(len(df.iloc[:, month_filter-1])):
        plt.xlabel('Jours de l\'année')
        plt.ylabel('Température (°C)')
        liste.append(df.iloc[day, month_filter-1])
        liste = [x for x in liste if str(x) != 'nan']
plt.title('Evolution annuelle de la température')
plt.plot(liste)
mplcursors.cursor()
plt.show()

#Comparaison avec Savukoski kirkonkyla
data_savukoski = pd.read_excel("./graph/Savukoski kirkonkyla.xlsx",sheet_name='Observation data')
df_savukoski = pd.DataFrame(data_savukoski)
df_savukoski['Jours'] = range(1, len(df_savukoski) + 1)
df_savukoski.plot(x ='Jours', y='Air temperature (degC)',label='Savukoski Kirkonkyla', color='black')
plt.plot(liste,label='Notre ville mystère',color='red')
plt.xlabel('Jours de l\'année')
plt.ylabel('Température (°C)')
plt.title('Evolution des températures de nos deux villes')
legend = plt.legend(loc='lower right', shadow=True, fontsize='x-large')
legend.get_frame().set_facecolor('C0')
mplcursors.cursor()
plt.show()

#Différence de moyenne de température sur l'année
for i in df_savukoski:
    curr_temp = list(df_savukoski.groupby("m")['Air temperature (degC)'].mean())
    index = 0
    total_temp = 0
    for temp in curr_temp :
        total_temp += abs(average[index]-temp)
        index +=1
print('Diff = ' + str(total_temp) + ' °C')



#Recherche d'une capitale ressemblant à notre ville mystère
df_capitale = pd.read_csv("./graph/city_temperature.csv")
df_capitale = df_capitale.drop_duplicates()

#Suppression des données inutiles
df_capitale = df_capitale[df_capitale.Day != 0]
df_capitale = df_capitale[df_capitale.Year == 2018]
df_capitale = df_capitale[df_capitale.Region == 'Europe']
df_capitale = df_capitale.drop(['Region','State','Year'],1)

#Récupération de la capitale la plus proche niveau température avec la ville mystère
df_capitale["AvgTemperature"] = (df_capitale["AvgTemperature"] - 32)/1.8
temp_mini = 100
ville = ""
ranking_city = []
for i in df_capitale.groupby("City") :
    df_city = pd.DataFrame(i[1])
    curr_temp = list(df_city.groupby("Month")['AvgTemperature'].mean())
    index = 0
    total_temp = 0
    for temp in curr_temp :
        total_temp += abs(average[index]-temp)
        index +=1
    if(temp_mini > total_temp) :
        temp_mini = total_temp
        ville = i[0]
        ranking_city.append([ville,temp_mini])
        df = pd.DataFrame(ranking_city, columns =['City', 'Diff °C'])
ax = df.plot.bar(x='City', y='Diff °C', rot=0)
plt.title('Classement des villes selon la différence de température')
mplcursors.cursor()
plt.show()   
print(str(ville) +' '+ str(temp_mini))
for day in range(len(df_capitale.iloc[:, 4])):
    if df_capitale.iloc[day, 4] < -50 :
        df_capitale.iloc[day, 4] = (df_capitale.iloc[day+1, 4] + df_capitale.iloc[day-1, 4])/2

chosen_one = df_capitale[df_capitale.City == ville]
chosen_one['Jours'] = range(1, len(chosen_one) + 1)
chosen_one.plot(x ='Jours', y='AvgTemperature',label=ville,color='black')
plt.plot(liste,label='Notre ville mystère',color='red')
plt.xlabel('Jours de l\'année')
plt.ylabel('Température (°C)')
plt.title('Evolution des températures de nos deux villes')
legend = plt.legend(loc='lower right', shadow=True, fontsize='x-large')
legend.get_frame().set_facecolor('C0')
mplcursors.cursor()
plt.show()

