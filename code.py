import pandas as pd

# Load the data
df = pd.read_csv('world_population.csv')

# Display the first 5 rows to verify
print(df.head())
# Verification des dimensions (lignes, colonnes)
print("Dimensions du dataset :", df.shape)

# Informations sur Les types de données et valeurs non nulles
print(df.info())
#Resume statistique des colonnes numeriques
print(df.describe())
print(df.isnull().sum())
import matplotlib.pyplot as plt

# Count number of countries per continent
continent_counts = df['Continent'].value_counts()

# Create pie chart
plt.figure(figsize=(8, 8))
plt.pie(continent_counts, labels=continent_counts.index, autopct='%1.1f%%')
plt.title("Répartition des pays par continent")
plt.show()
# Tri et sélection
top10 = df.sort_values('2022 Population', ascending=False).head(10)

# Barplot
plt.figure(figsize=(12, 6))
plt.barn(top10['Country/Territory'], top10['2022 Population'], color='skyblue')
plt.xlabel('Population (2022)')
plt.title('Top 10 des pays par population en 2022')
plt.gca().invert_yaxis() # Du plus grand au plus petit
plt.show()
print("Valeurs manquantes :")
print(df.isnull().sum())
print("\nDoublons :", df.duplicated().sum())
# Nettoyage des textes
df['Country/Territory'] = df['Country/Territory'].str.strip()
# Conversion des nombres
df['2022 Population'] = df['2022 Population'].astype('int64')
df.to_csv('population_clean.csv',index=False)
population_continent = df.groupby('Continent')['2022 Population'].sum().sort_values(ascending=False)
print(population_continent)
import matplotlib.pyplot as plt
df['2022 Population'].plot(kind='hist', bins=50, figsize=(10,6))
plt.title('Distribution des populations nationales (2022)')
plt.xlabel('Population')
plt.ylabel('Nombre de pays')
plt.show()
# Calcul du VRAI taux de croissance moyen en %
taux_croissance_pct = (df['Growth Rate'].mean() - 1) * 100

print(f"Taux de croissance démographique moyen annuel : {taux_croissance_pct:.2f}%")
# Calculate median density
densite_mediane = df['Density (per km²)'].median()
print(f"Densité médiane : {densite_mediane:.1f} hab/km²")

pays_100m = df[df['2022 Population'] > 100_000_000].copy()

# Display summary
print(f"\n{len(pays_100m)} pays dépassent 100 millions d'habitants :")
print(pays_100m[['Country/Territory', '2022 Population']].sort_values('2022 Population', ascending=False))
import numpy as np
import matplotlib.pyplot as plt

# 1. Create growth column 2000-2022
df['Croissance_2000_2022'] = ((df['2022 Population'] - df['2000 Population']) / df['2000 Population']) * 100

# 2. Population size categorization
conditions = [
    df['2022 Population'] < 1_000_000,
    df['2022 Population'] < 10_000_000,
    df['2022 Population'] < 100_000_000,
    df['2022 Population'] >= 100_000_000
]
labels = ['<1M', '1-10M', '10-100M', '>100M']
df['Taille_Pays'] = np.select(conditions, labels)

# Display new columns
print("\nNouvelle colonne 'Croissance_2000_2022' (extrait) :")
print(df[['Country/Territory', '2000 Population', '2022 Population', 'Croissance_2000_2022']]
      .sort_values('Croissance_2000_2022', ascending=False).head())
print("\nRépartition des pays par catégorie de taille :")
print(df['Taille_Pays'].value_counts().sort_index())

# 4. Visualization
plt.figure(figsize=(12, 6))

# Growth histogram
plt.subplot(1, 2, 1)
df['Croissance_2000_2022'].plot(kind='hist', bins=30, color='skyblue')
plt.title('Distribution des croissances 2000-2022')
plt.xlabel('% Croissance')

# Size pie chart
plt.subplot(1, 2, 2)
df['Taille_Pays'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Répartition par taille de population')
plt.ylabel('')
plt.tight_layout()
plt.show()
# Grouping by size category
taille_stats = df.groupby('Taille_Pays')['2022 Population'].agg(['sum', 'count'])

# Pie chart
plt.figure(figsize=(8, 8))
plt.pie(taille_stats['sum'], 
        labels=taille_stats.index, 
        autopct='%1.1f%%',
        startangle=90, 
        colors=['lightgreen', 'lightblue', 'orange', 'pink'])
plt.title('Répartition de la population mondiale\npar taille de pays (2022)')
plt.show()












