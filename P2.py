import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('voetbal.xlsx', sheet_name='gegevens')
#print(data.head())
#print(data.values)

#generen van geboortedatums, tussen 01/01/2011 en 31/12/2011
pd.date_range(start='01/01/2011', end='31/12/2011')


#geboortedatums bij speler zetten in excel file
data["geboortedatum"] = np.random.choice(pd.date_range(start='01/01/2011', end='31/12/2011'),len(data))

data['geboortedatum'] = pd.to_datetime(data['geboortedatum'])

#kolom inzet generen met 3 mogelijke categorieën
data.loc[(data['geboortedatum'] >= '2011-01-01') & (data['geboortedatum'] <= '2011-03-31'),"inzet"] = "zeer goed"
data.loc[(data['geboortedatum'] >= '2011-04-01') & (data['geboortedatum'] <= '2011-06-30'),"inzet"] = "goed"
data.loc[(data['geboortedatum'] >= '2011-07-01') & (data['geboortedatum'] <= '2011-09-30'),"inzet"] = "goed"
data.loc[(data['geboortedatum'] >= '2011-10-01') & (data['geboortedatum'] <= '2011-12-31'),"inzet"] = "matig"


#grafiek maken lengte & gewicht
plt.xlabel('gewicht')
plt.ylabel('lengte')
plt.scatter(data['gewicht'] ,data['lengte'] ,color='DarkBlue')
plt.show()
data.to_excel('voetbalNieuw1.xlsx',sheet_name='P1')


#Staafdiagram met aantal gemaakte goalen per positie
#Maak in python een staafdiagram van het aantal gemaakte goalen per positie.
#Deel de posities telkens ook nog op naar geboortecategorie en bespreek

plt.bar(data['positie'],data['aantal gemaakte goalen'])
plt.xlabel('positie')
plt.ylabel('# goals')
plt.show()



