import pandas as pd
import matplotlib.pyplot as plt

loaded_data = pd.read_csv("dataset/owid-covid-data.csv")
print(loaded_data)
print("Columns:\n", loaded_data.columns)
print("first 5 rows:\n", loaded_data.head())
print(loaded_data.isnull().sum())

#filter for selected countries
countries = ['Kenya', 'United States', 'India']
df_filtered = loaded_data[loaded_data['location'].isin(countries)]
print(df_filtered)

# Drop rows with missing critical values
df_filtered = df_filtered.dropna(subset=['total_cases', 'total_deaths', 'total_vaccinations'])
print("new df_filter\n",df_filtered)


# Fill missing numeric values with 0
df_filtered[['new_cases', 'new_deaths']] = df_filtered[['new_cases', 'new_deaths']].fillna(0)



# Plot total cases over time for each country
plt.figure(figsize=(12, 6))
for country in countries:
    country_data = df_filtered[df_filtered['location'] == country]
    plt.plot(country_data['date'], country_data['total_cases'], label=country)

plt.title('Total COVID-19 Cases Over Time')
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

df_filtered['death_rate'] = df_filtered['total_deaths'] / df_filtered['total_cases']

# Plot total vaccinations over time for each country
plt.figure(figsize=(12, 6))
for country in countries:
    country_data = df_filtered[df_filtered['location'] == country]
    plt.plot(country_data['date'], country_data['total_vaccinations'], label=country)

plt.title('Total COVID-19 Vaccinations Over Time')
plt.xlabel('Date')
plt.ylabel('Total Vaccinations')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

