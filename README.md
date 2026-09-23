# 🌍 World Population Analysis

This project performs an exploratory data analysis (EDA) of world population data using **Python, Pandas, NumPy, and Matplotlib**.

The objective is to explore population distribution across countries and continents, identify the most populated countries, analyze population growth, and classify countries according to their population size.

## 📊 Project Overview

The analysis includes:

* Loading and inspecting the population dataset
* Checking dataset dimensions and data types
* Generating descriptive statistics
* Detecting missing values and duplicates
* Cleaning country names and numerical data
* Analyzing population by continent
* Identifying the 10 most populated countries in 2022
* Analyzing the distribution of national populations
* Calculating average population growth
* Calculating median population density
* Identifying countries with more than 100 million inhabitants
* Calculating population growth between 2000 and 2022
* Categorizing countries according to population size
* Creating visualizations using Matplotlib

## 🛠️ Technologies Used

* **Python 3**
* **Pandas** – data manipulation and analysis
* **NumPy** – numerical operations
* **Matplotlib** – data visualization

## 📁 Dataset

The project uses a CSV file called:

```text
world_population.csv
```

The dataset contains population-related information for countries and territories, including:

* Country/Territory
* Continent
* 2000 Population
* 2022 Population
* Growth Rate
* Density (per km²)

## 🔍 Data Exploration

The dataset is initially loaded using Pandas:

```python
import pandas as pd

df = pd.read_csv('world_population.csv')

print(df.head())
print("Dimensions du dataset :", df.shape)
print(df.info())
print(df.describe())
print(df.isnull().sum())
```

This allows us to understand the structure, size, data types, statistical characteristics, and missing values of the dataset.

## 🧹 Data Cleaning

The project checks for missing values and duplicate rows:

```python
print("Valeurs manquantes :")
print(df.isnull().sum())

print("\nDoublons :", df.duplicated().sum())
```

Country names are cleaned by removing unnecessary spaces:

```python
df['Country/Territory'] = df['Country/Territory'].str.strip()
```

The 2022 population column is converted to an integer:

```python
df['2022 Population'] = df['2022 Population'].astype('int64')
```

The cleaned dataset is then exported:

```text
population_clean.csv
```

## 🌎 Population by Continent

The project calculates the total population for each continent:

```python
population_continent = (
    df.groupby('Continent')['2022 Population']
    .sum()
    .sort_values(ascending=False)
)

print(population_continent)
```

A pie chart is also used to visualize the number of countries belonging to each continent.

## 👥 Top 10 Most Populated Countries

The project identifies the 10 countries with the largest populations in 2022:

```python
top10 = df.sort_values(
    '2022 Population',
    ascending=False
).head(10)
```

A bar chart is then created to visualize the results.

> **Note:** Use `plt.bar()` rather than `plt.barn()` in the original code.

Example:

```python
plt.bar(
    top10['Country/Territory'],
    top10['2022 Population']
)
```

## 📈 Population Distribution

A histogram is used to visualize the distribution of national populations in 2022:

```python
df['2022 Population'].plot(
    kind='hist',
    bins=50,
    figsize=(10, 6)
)

plt.title('Distribution des populations nationales (2022)')
plt.xlabel('Population')
plt.ylabel('Nombre de pays')
plt.show()
```

## 📊 Population Growth

The average annual growth rate is calculated from the `Growth Rate` column:

```python
taux_croissance_pct = (df['Growth Rate'].mean() - 1) * 100

print(
    f"Taux de croissance démographique moyen annuel : "
    f"{taux_croissance_pct:.2f}%"
)
```

The project also calculates population growth between 2000 and 2022:

```python
df['Croissance_2000_2022'] = (
    (df['2022 Population'] - df['2000 Population'])
    / df['2000 Population']
) * 100
```

This provides the percentage change in population over the period.

## 🏙️ Population Density

The median population density is calculated using:

```python
densite_mediane = df['Density (per km²)'].median()

print(f"Densité médiane : {densite_mediane:.1f} hab/km²")
```

## 🌐 Countries With More Than 100 Million Inhabitants

The project identifies countries whose 2022 population exceeds 100 million:

```python
pays_100m = df[
    df['2022 Population'] > 100_000_000
].copy()
```

The countries are then sorted by population.

## 📏 Population Size Categories

Countries are divided into four categories:

| Category  |          Population |
| --------- | ------------------: |
| `<1M`     | Less than 1 million |
| `1-10M`   |        1–10 million |
| `10-100M` |      10–100 million |
| `>100M`   | 100 million or more |

The categories are created using NumPy:

```python
conditions = [
    df['2022 Population'] < 1_000_000,
    df['2022 Population'] < 10_000_000,
    df['2022 Population'] < 100_000_000,
    df['2022 Population'] >= 100_000_000
]

labels = ['<1M', '1-10M', '10-100M', '>100M']

df['Taille_Pays'] = np.select(
    conditions,
    labels
)
```

## 📊 Visualizations

The project produces several visualizations:

1. Countries by continent
2. Top 10 countries by population
3. Distribution of national populations
4. Population growth distribution from 2000–2022
5. Distribution of countries by population size
6. World population distribution by country-size category

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/world-population-analysis.git
cd world-population-analysis
```

Install the required libraries:

```bash
pip install pandas numpy matplotlib
```

## ▶️ Run the Project

Make sure `world_population.csv` is located in the project directory.

Then run:

```bash
python main.py
```

## 📂 Project Structure

```text
world-population-analysis/
│
├── world_population.csv
├── population_clean.csv
├── main.py
├── README.md
└── requirements.txt
```

Example `requirements.txt`:

```text
pandas
numpy
matplotlib
```

## 🎯 Learning Objectives

This project demonstrates practical skills in:

* Data loading
* Data cleaning
* Exploratory Data Analysis (EDA)
* Pandas DataFrames
* Data filtering and sorting
* GroupBy operations
* Statistical analysis
* Feature engineering
* Data visualization
* Working with CSV datasets
* Python data analysis

## 🚀 Possible Improvements

Future versions could include:

* Interactive dashboards with **Streamlit**
* Interactive charts with **Plotly**
* Correlation analysis between population, density, and growth
* Geographic visualization using maps
* Analysis of population evolution over multiple years
* Machine Learning models for population prediction
* A web application for exploring the dataset

## 👨‍💻 Author

**Oussama Al Azhari**

AI & 3D Printing Graduate

Interested in:

* Artificial Intelligence
* Machine Learning
* Deep Learning
* Data Science
* AI Agents
* Python

---

⭐ If you find this project useful, feel free to give it a star!
