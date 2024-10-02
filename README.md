# Data Cleaning and Preprocessing Project

## Project Overview

This project demonstrates a typical **data cleaning and preprocessing** workflow using a real-world dataset. The dataset used in this project is the famous Titanic dataset, which contains information about passengers aboard the RMS Titanic. The main objective of this project is to showcase essential data cleaning techniques that are often applied in data science and data analysis projects.

Key steps performed in the project:
1. **Handling missing values**: Filling missing data using appropriate methods (median for numerical columns, mode for categorical columns).
2. **Correcting data types**: Transforming categorical variables into numerical types for analysis or modeling.
3. **Outlier detection**: Removing outliers based on domain knowledge.
4. **Feature scaling**: Normalizing features to ensure that they are on the same scale, making them suitable for machine learning models.

## Files in This Repository

- **data_cleaning.py**: This is the main Python script that loads the dataset, cleans it, and performs the preprocessing tasks outlined above.
- **cleaned_titanic_data.csv**: The cleaned dataset after running the data cleaning script.
- **README.md**: This file, providing an overview of the project.

## How to Run the Project

1. **Install Required Libraries**:
   Ensure you have the following libraries installed:
   ```bash
   pip install pandas numpy scikit-learn