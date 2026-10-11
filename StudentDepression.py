    
# Data Science
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns    

try:
    data = pd.read_csv('Student Depression Dataset.csv')
    print(" Dataset successfully loaded!")
except FileNotFoundError:
    print(" Error: 'Student Depression Dataset.csv' file not found!")
    print("Please check if the file is in the current folder.")
    exit()
    
print("\n Dataset Head (First five rows):")
print("=" * 50)
print(data.head())
print("\n Dataset Information:")
print("=" * 50)
print(data.info())

print("\n Statistical Summary:")
print("=" * 50)
print(data.describe())

print("\n Columns in dataset:")
print("=" * 50)
for col in data.columns:
    print(f" . {col}")    
    
print("\n Plotting Histograms for Numerical Columns...")    
print("=" * 50)

numerical_columns = ['Age', 'Academic Pressure', 'Work Pressure', 
                     'CGPA', 'Study Satisfaction', 'Job Satisfaction',
                     'Work/Study Hours', 'Financial Stress'] 

for column in numerical_columns:
    if column in data.columns:
        plt.figure(figsize=(8,5))
        data[column].hist(bins=20, edgecolor='black', color='skyblue')
        plt.title(f'Distribution of {column}', fontsize=14, fontweight='bold')
        plt.xlabel(column, fontsize=12)
        plt.ylabel('Frequency', fontsize=12) 
        plt.grid(True, alpha=0.3)
        plt.show()
        
    else:
        print(f" Column '{column}' not found in dataset.")
        
print("\n Categorical Columns Analysis:")
print("=" * 50) 

categorical_columns = ['Gender', 'City', 'Profession', 'Sleep Duration',
                       'Dietary Habits', 'Degree',
                       'Have you ever had suicidal thoughts',
                       'Family History of Mental Illness', 'Depression']

for column in categorical_columns:
    if column in data.columns:
        print(f"\n {column}:")
        print(data[column].value_counts())
        
        plt.figure(figsize=(10, 6))
        sns.countplot(x=column, data=data, palette='viridis')
        plt.title(f'Count of {column}', fontsize=14, fontweight='bold')
        plt.xlabel(column, fontsize=12)
        plt.ylabel('Count', fontsize=12)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()
        
print("\n DEPRESSION ANALYSIS:")
print("=" * 50)

if 'Depression' in data.columns:
    depression_counts = data['Depression'].value_counts()
    
    print("\nDepression Statistics:")
    print(f"  - Students with Depression: {depression_counts.get(1, depression_counts.get('Yes', 0))}")   
    print(f"  - Students without Depression: {depression_counts.get(0, depression_counts.get('No', 0))}")       
    
    plt.figure(figsize=(8, 8))
    colors = ['#ff9999', '#66b3ff']
    labels = ['Depression', 'No Depression']
    sizes = [depression_counts.get(1, depression_counts.get('Yes', 0)),
             depression_counts.get(0, depression_counts.get('No', 0))]
    
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%',
            startangle=90, explode=(0.05, 0))
    plt.title('Depression Distribution Among Students', fontsize=14, fontweight='bold')
    plt.show()
    
if 'Gender' in data.columns and 'Depression' in data.columns:
    print("\n Gender-wise Depression Analysis:")
    print("=" * 50)

    gender_depression = pd.crosstab(data['Gender'], data['Depression'])
    print(gender_depression)

    gender_depression.plot(kind='bar', stacked=True, figsize=(10, 6),
                           color=['#66b3ff', '#ff9999'])
    
    plt.title('Depression by Gender', fontsize=14, fontweight='bold')
    plt.xlabel('Gender', fontsize=12)
    plt.ylabel('Count', fontsize=12)
    plt.xticks(rotation=0)
    plt.legend(title='Depression')
    plt.tight_layout()
    plt.show()
    
print("\n Correlation Analysis:")
print("=" * 50)

numerical_data = data.select_dtypes(include=[np.number])

if len(numerical_data.columns) > 1:
    correlation_matrix = numerical_data.corr()

    plt.figure(figsize=(12, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm',
                center=0, fmt='.2f', square=True)

    plt.title('Correlation Matrix of Numerical Features', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()
    
if 'Depression' in correlation_matrix.columns:
    print("\n Features most correlated with Depression:")
    depression_corr = correlation_matrix['Depression'].sort_values(ascending=False)
    for feature, corr in depression_corr.items():
        if feature != 'Depression':
            print(f" • {feature}: {corr:.3f}")

print("\n" + "=" * 50)
print(" ANALYSIS COMPLETE!")
print("=" * 50)  