# Student Mental Health & Well-being EDA Dashboard
An exploratory data analysis (EDA) pipeline built in Python to evaluate demographic, academic, and lifestyle factors impacting student mental health and depression trends.

Project Overview:
This project processes student record datasets to clean, manipulate, and analyze multi-variable psychological and lifestyle parameters. Using statistical correlation and data visualization libraries, the script uncovers key risk factors linked to student stress and depression.

Technologies Used:
Python (Core programming, exception handling)
Pandas & NumPy (Data cleaning, transformation, and statistical aggregation)
Matplotlib & Seaborn (Univariate distributions, categorical count plots, proportional pie charts, and correlation heatmaps)

Key Features & Visualizations:
Data Ingestion & Cleaning: Robust file handling with missing value evaluation and data type inspections.
Univariate Analysis: Custom histograms for numerical features (Age, CGPA, Study Satisfaction, Work/Study Hours).
Categorical Breakdowns: Count plots and frequency distributions across gender, profession, dietary habits, and sleep duration.
Targeted Insights: Proportional pie charts evaluating depression prevalence and gender-wise stacked bar charts.
Correlation Matrix: Annotated Seaborn heatmap isolating the primary variables most strongly correlated with student depression.

How to Run the Code:
1. Clone the repository or download the files.
2. Ensure you have the required libraries installed:
   ```bash
   pip install pandas numpy matplotlib seaborn


   python StudentDepression.py
