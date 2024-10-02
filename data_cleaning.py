# data_cleaning.py

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# Load dataset (replace this with your dataset)
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df = pd.read_csv(url)

# Display the first 5 rows of the dataset
print("Initial Dataset:")
print(df.head())

# 1. Handle Missing Values
# Fill missing values in 'Age' column with the median
df['Age'].fillna(df['Age'].median(), inplace=True)

# Fill missing values in 'Embarked' with the mode
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# 2. Correct Data Types
# Convert 'Sex' to a binary numeric column (Male = 1, Female = 0)
df['Sex'] = df['Sex'].apply(lambda x: 1 if x == 'male' else 0)

# Convert 'Embarked' to numeric categories
df['Embarked'] = df['Embarked'].astype('category').cat.codes

# 3. Handle Outliers (Remove any age over 75 as an outlier for this case)
df = df[df['Age'] <= 75]

# 4. Normalize/Scale Features (Only numeric columns, excluding target)
scaler = StandardScaler()
df[['Age', 'Fare']] = scaler.fit_transform(df[['Age', 'Fare']])

# Display cleaned and preprocessed dataset
print("Cleaned and Preprocessed Dataset:")
print(df.head())

# Save the cleaned dataset for further use
df.to_csv('cleaned_titanic_data.csv', index=False)

print("Data cleaning and preprocessing complete. Cleaned data saved as 'cleaned_titanic_data.csv'.")