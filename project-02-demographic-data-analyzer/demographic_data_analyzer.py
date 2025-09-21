"""
project-02-demographic-data-analyzer/demographic_data_analyzer.py

Simple and robust solution for FreeCodeCamp's "Demographic Data Analyzer".
Save this file in the same folder as demographic_data.csv.
"""

import os
import pandas as pd

def calculate_demographic_data(print_data=True):
    # 1) Find the path to the CSV file (works even if you run the script from repo root)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(script_dir, "demographic_data.csv")

    # Column names for the UCI Adult dataset (the file usually doesn't have headers)
    columns = [
        "age", "workclass", "fnlwgt", "education", "education-num",
        "marital-status", "occupation", "relationship", "race",
        "sex", "capital-gain", "capital-loss", "hours-per-week",
        "native-country", "salary"
    ]

    # 2) Read the CSV (skipinitialspace removes extra spaces after commas)
    df = pd.read_csv(data_path, names=columns, header=None, skipinitialspace=True)

    # 3) Clean string columns (remove stray spaces)
    str_cols = ["workclass", "education", "marital-status", "occupation",
                "relationship", "race", "sex", "native-country", "salary"]
    for c in str_cols:
        df[c] = df[c].astype(str).str.strip()

    # ----- Calculations (one-by-one, explained simply) -----

    # How many of each race?
    race_count = df["race"].value_counts()

    # Average age of men (rounded to 1 decimal)
    average_age_men = round(df[df["sex"] == "Male"]["age"].mean(), 1)

    # Percentage with Bachelor's degree (rounded to 1 decimal)
    percentage_bachelors = round((df["education"] == "Bachelors").mean() * 100, 1)

    # People with advanced education
    higher_edu_mask = df["education"].isin(["Bachelors", "Masters", "Doctorate"])
    # Percentage of those with advanced education who earn >50K
    higher_education_rich = round((df[higher_edu_mask]["salary"] == ">50K").mean() * 100, 1)

    # Percentage of those without advanced education who earn >50K
    lower_education_rich = round((df[~higher_edu_mask]["salary"] == ">50K").mean() * 100, 1)

    # Minimum hours per week
    min_work_hours = df["hours-per-week"].min()

    # Percentage of rich (>50K) among those who work the minimum hours
    min_workers = df[df["hours-per-week"] == min_work_hours]
    if len(min_workers) == 0:
        rich_percentage_min_workers = 0.0
    else:
        rich_percentage_min_workers = round((min_workers["salary"] == ">50K").mean() * 100, 1)

    # Country with highest percentage of people earning >50K
    country_counts = df["native-country"].value_counts()
    country_rich_counts = df[df["salary"] == ">50K"]["native-country"].value_counts()

    # compute percentage per country and get the top one
    country_percentages = (country_rich_counts / country_counts * 100).dropna()
    if len(country_percentages) == 0:
        highest_earning_country = None
        highest_earning_country_percentage = 0.0
    else:
        highest_earning_country = country_percentages.idxmax()
        highest_earning_country_percentage = round(country_percentages.max(), 1)

    # Most popular occupation for those who earn >50K in India
    ind_high_earners = df[(df["native-country"] == "India") & (df["salary"] == ">50K")]
    if len(ind_high_earners) == 0:
        top_IN_occupation = None
    else:
        top_IN_occupation = ind_high_earners["occupation"].value_counts().idxmax()

    # Print results (if desired)
    if print_data:
        print("Number of each race:\n", race_count.to_string())
        print("\nAverage age of men:", average_age_men)
        print("Percentage with Bachelors degrees:", f"{percentage_bachelors}%")
        print("Percentage with higher education that earn >50K:", f"{higher_education_rich}%")
        print("Percentage without higher education that earn >50K:", f"{lower_education_rich}%")
        print("Min work hours:", min_work_hours)
        print("Percentage of rich among those who work minimum hours:", f"{rich_percentage_min_workers}%")
        print("Country with highest % of rich people:", highest_earning_country)
        print("Highest % of rich people in country:", f"{highest_earning_country_percentage}%")
        print("Top occupation in India for those who earn >50K:", top_IN_occupation)

    # return values as a dictionary (useful for tests later)
    return {
        "race_count": race_count,
        "average_age_men": average_age_men,
        "percentage_bachelors": percentage_bachelors,
        "higher_education_rich": higher_education_rich,
        "lower_education_rich": lower_education_rich,
        "min_work_hours": min_work_hours,
        "rich_percentage_min_workers": rich_percentage_min_workers,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage": highest_earning_country_percentage,
        "top_IN_occupation": top_IN_occupation
    }


if __name__ == "__main__":
    calculate_demographic_data(print_data=True)

