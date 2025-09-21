import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------
# 1. Import the dataset
# -------------------------------
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=['date'], index_col='date')

# -------------------------------
# 2. Clean the data
# -------------------------------
# Keep only data within the 2.5th and 97.5th percentiles
lower = df['value'].quantile(0.025)
upper = df['value'].quantile(0.975)
df = df[(df['value'] >= lower) & (df['value'] <= upper)]

# -------------------------------
# 3. Line Plot
# -------------------------------
def draw_line_plot():
    fig, ax = plt.subplots(figsize=(15,5))
    ax.plot(df.index, df['value'], color='red')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    plt.tight_layout()
    return fig

# -------------------------------
# 4. Bar Plot
# -------------------------------
def draw_bar_plot():
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month

    # Group by year and month, take mean
    df_bar = df_bar.groupby(['year','month'])['value'].mean().unstack()

    # Plot
    fig = df_bar.plot(kind='bar', figsize=(12,7)).get_figure()
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend([
        'January','February','March','April','May','June',
        'July','August','September','October','November','December'
    ], title='Months')
    plt.tight_layout()
    return fig

# -------------------------------
# 5. Box Plot
# -------------------------------
def draw_box_plot():
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = df_box['date'].dt.year
    df_box['month'] = df_box['date'].dt.strftime('%b')

    # Sort months in calendar order
    month_order = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

    fig, axes = plt.subplots(1,2, figsize=(15,5))

    # Year-wise box plot
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    # Month-wise box plot
    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1], order=month_order)
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    plt.tight_layout()
    return fig

# -------------------------------
# Optional: Test plots
# -------------------------------
if __name__ == "__main__":
    draw_line_plot()
    draw_bar_plot()
    draw_box_plot()
    plt.show()
