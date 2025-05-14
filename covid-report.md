# 🌍 COVID-19 Global Trends Analysis

## 📘 Project Overview

This project analyzes the global trends of the COVID-19 pandemic using a real-world dataset provided by [Our World in Data](https://ourworldindata.org/coronavirus). The dataset includes statistics on cases, deaths, and vaccinations across multiple countries over time.

---

## 🎯 Objectives

- ✅ Import and clean global COVID-19 data.
- ✅ Analyze time trends (cases, deaths, and vaccinations).
- ✅ Compare metrics across selected countries (Kenya, India, United States).
- ✅ Visualize trends using line and bar charts.
- ✅ Summarize insights in a structured report.

---

## 📁 Dataset Info

- **File name**: `owid-covid-data.csv`
- **Path**: `dataset/owid-covid-data.csv`
- **Source**: Our World in Data
- **Key columns**:
  - `date`, `location`, `total_cases`, `total_deaths`
  - `new_cases`, `new_deaths`
  - `total_vaccinations`, `people_vaccinated_per_hundred`

```python
import pandas as pd

#import pandas as pd

# Load dataset
loaded_data = pd.read_csv("dataset/owid-covid-data.csv")
loaded_data.columns
loaded_data.head()


#Data cleaning
oaded_data['date'] = pd.to_datetime(loaded_data['date'])
countries = ['Kenya', 'India', 'United States']
loaded_data = loaded_data[loaded_data['location'].isin(countries)]

loaded_data = loaded_data[['location', 'date', 'total_cases', 'new_cases',
         'total_deaths', 'new_deaths', 'total_vaccinations',
         'people_vaccinated_per_hundred']]

loaded_data = loaded_data.fillna(0)  # Replace missing values with 0


#exploratory data analysis
import matplotlib.pyplot as plt

for country in countries:
    subset = loaded_data[loaded_data['location'] == country]
    plt.plot(subset['date'], subset['total_cases'], label=country)

plt.title('Total COVID-19 Cases Over Time')
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("images/total_cases_over_time.png")
plt.show()


#total deatrhs over time
for country in countries:
    subset = loaded_data[loaded_data['location'] == country]
    plt.plot(subset['date'], subset['total_deaths'], label=country)

plt.title('Total COVID-19 Deaths Over Time')
plt.xlabel('Date')
plt.ylabel('Total Deaths')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("images/total_deaths_over_time.png")
plt.show()


#vaccination progress
for country in countries:
    subset = loaded_data[loaded_data['location'] == country]
    plt.plot(subset['date'], subset['people_vaccinated_per_hundred'], label=country)

plt.title('% of Population Vaccinated Over Time')
plt.xlabel('Date')
plt.ylabel('People Vaccinated per 100')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("images/vaccination_progress.png")
plt.show()


#key findings
The United States had the highest number of cases and deaths overall.

India experienced the steepest spike in daily cases during the Delta wave.

Kenya had a slower rise in cases but lower vaccination coverage compared to others.

Vaccination progress in the U.S. and India increased rapidly from early 2021, while Kenya’s rate was significantly lower throughout 2021.

#tools used
pandas: Data loading and manipulation

matplotlib: Visualizations
