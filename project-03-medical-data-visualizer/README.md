# Project 03 – Medical Data Visualizer

## Overview
This project is part of **freeCodeCamp’s Data Analysis with Python** certification.  
The goal is to **analyze and visualize medical data** to understand patient characteristics, detect outliers, and explore relationships between health metrics and cardiovascular disease.

## Dataset
- **File:** `medical_examination.csv`  
- **Description:** Contains patient medical measurements including:  
  - `age`, `height`, `weight`  
  - Blood pressure: `ap_hi`, `ap_lo`  
  - Cholesterol, glucose, alcohol consumption, smoking, activity  
  - Cardiovascular disease indicator: `cardio`  

## Project Tasks
1. **Add Overweight Column**  
   - Calculate BMI: `weight / (height in meters)^2`  
   - Assign `1` if BMI > 25 (overweight), else `0`.  

2. **Normalize Data**  
   - Cholesterol and glucose: `0 = good`, `1 = bad`.  

3. **Categorical Plot**  
   - Visualize counts of cholesterol, glucose, alcohol, smoking, activity, and overweight.  
   - Compare distributions for patients with `cardio = 0` and `cardio = 1`.  

4. **Heat Map**  
   - Clean data by removing:  
     - Diastolic pressure > systolic  
     - Height and weight outliers (outside 2.5th–97.5th percentiles)  
   - Calculate correlation matrix and visualize relationships using a heatmap.  

## Technologies Used
- **Python 3.x**  
- **pandas** – Data manipulation  
- **matplotlib** – Plotting  
- **seaborn** – Statistical visualization  
- **numpy** – Numerical operations  

## How to Run
1. Install dependencies:  
```bash
pip install pandas matplotlib seaborn numpy
