# Pre requisites:
1) Python 
2) pip - command line tool for python

# To install necessary libraries:
pip3 install pandas

Note: Please disconnect from any VPN connections before running the program

## Intent: 
In this activity, you’ll clean a small dataset by handling missing values, duplicates, and standardizing formats.

# Explanation of the Code

This Python script demonstrates a workflow for cleaning a dataset using the `pandas` library. Below is a detailed explanation:

---

## 1. **Importing pandas**
```python
import pandas as pd
```
- This imports the `pandas` library, a powerful tool for data manipulation and analysis.

---

## 2. **Creating and Loading the Dataset**
```python
data = {
    "Name": ["Alice", "Bob", None, "Eve", "Alice"],
    "Age": [30, 25, 40, 30, 30],
    "City": ["New York", None, "Los Angeles", "San Francisco", "New York"],
    "Salary": [85000, 70000, 65000, 90000, 85000],
}
df = pd.DataFrame(data)
print("Original Data:\n", df)
```
- A dictionary named `data` is created to represent a small dataset with the following columns: `Name`, `Age`, `City`, and `Salary`.
- The `pd.DataFrame(data)` command converts the dictionary into a pandas DataFrame, which is a tabular data structure.
- The original dataset is printed to show its initial state.

---

## 3. **Handling Missing Values**
```python
df["Name"].fillna("Unknown", inplace=True)
df["City"].fillna("Unknown", inplace=True)
```
- **Purpose:** Replaces missing (`None` or `NaN`) values in the `Name` and `City` columns.
- The `fillna` method is used:
  - Missing values are replaced with the string `"Unknown"`.
  - `inplace=True` modifies the DataFrame directly without requiring reassignment.

---

## 4. **Removing Duplicates**
```python
df = df.drop_duplicates()
```
- **Purpose:** Removes rows that are exact duplicates of previous rows.
- The `drop_duplicates()` method ensures each row in the DataFrame is unique.

---

## 5. **Standardizing Formatting**
```python
df["City"] = df["City"].str.title()
```
- **Purpose:** Standardizes text data in the `City` column by capitalizing the first letter of each word.
- The `str.title()` method transforms strings like `"new york"` into `"New York"`.

---

## 6. **Converting Data Types**
```python
df["Age"] = df["Age"].astype(int)
```
- **Purpose:** Ensures the `Age` column's data type is `int`. This step is optional but can prevent errors during further processing or analysis.

---

## 7. **Displaying Cleaned Data**
```python
print("\nCleaned Data:\n", df)
```
- Prints the cleaned version of the dataset after applying all the transformations.

---

## Output Explanation

### Original Data:
```plaintext
     Name  Age             City  Salary
0   Alice   30        New York   85000
1     Bob   25            None   70000
2    None   40     Los Angeles   65000
3     Eve   30  San Francisco   90000
4   Alice   30        New York   85000
```

### Cleaned Data:
```plaintext
     Name  Age             City  Salary
0   Alice   30        New York   85000
1     Bob   25         Unknown   70000
2  Unknown   40     Los Angeles   65000
3     Eve   30  San Francisco   90000
```

---

## Key Takeaways

1. **Data Cleaning:** This script demonstrates how to handle missing values, remove duplicates, and standardize formatting to ensure data quality.
2. **Efficiency:** `pandas` provides intuitive methods for common data cleaning tasks.
3. **Flexibility:** These operations can be tailored to suit specific datasets or requirements.

