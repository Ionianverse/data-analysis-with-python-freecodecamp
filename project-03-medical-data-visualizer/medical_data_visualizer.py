
# medical_data_visualizer.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1. Import the dataset
df = pd.read_csv("medical_examination.csv")

# 2. Add overweight column
df['overweight'] = (df['weight'] / (df['height']/100)**2 > 25).astype(int)

# 3. Normalize data (0 = good, 1 = bad)
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# 4. Function to draw categorical plot
def draw_cat_plot():
    # Melt the DataFrame
    df_cat = pd.melt(
        df,
        id_vars=['cardio'],
        value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
    )

    # Group and count
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

    # Draw the catplot
    fig = sns.catplot(
        data=df_cat,
        x='variable', y='total', hue='value', col='cardio',
        kind='bar'
    ).fig

    return fig

# 5. Function to draw heat map
def draw_heat_map():
    # Clean the data
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # Correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(corr)

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 10))

    # Draw the heatmap
    sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", square=True)

    return fig

# Optional: test plots by calling functions
if __name__ == "__main__":
    draw_cat_plot()
    draw_heat_map()
    plt.show()
