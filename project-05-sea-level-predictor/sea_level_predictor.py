import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# -------------------------------
# 1. Import the dataset
# -------------------------------
df = pd.read_csv('epa-sea-level.csv')

# -------------------------------
# 2. Scatter Plot
# -------------------------------
plt.figure(figsize=(12,6))
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue')
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')

# -------------------------------
# 3. Line of Best Fit (Full Dataset)
# -------------------------------
# Linear regression on all data
slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

# Predict values through 2050
years_extended = pd.Series(range(df['Year'].min(), 2051))
line_full = intercept + slope * years_extended

plt.plot(years_extended, line_full, color='red', label='Fit 1880 - Present')

# -------------------------------
# 4. Line of Best Fit (From 2000)
# -------------------------------
df_recent = df[df['Year'] >= 2000]
slope2, intercept2, r_value2, p_value2, std_err2 = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])

years_recent = pd.Series(range(2000, 2051))
line_recent = intercept2 + slope2 * years_recent

plt.plot(years_recent, line_recent, color='green', label='Fit 2000 - Present')

plt.legend()
plt.tight_layout()

# -------------------------------
# 5. Show Plot
# -------------------------------
plt.show()
