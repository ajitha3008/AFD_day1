import pandas as pd

# Load data
data = {
    "Name": ["Alice", "Bob", None, "Eve", "Alice"],
    "Age": [30, 25, 40, 30, 30],
    "City": ["New York", None, "Los Angeles", "San Francisco", "New York"],
    "Salary": [85000, 70000, 65000, 90000, 85000],
}
df = pd.DataFrame(data)
print("Original Data:\n", df)

# 1. Handle missing values (correct approach)
df["Name"] = df["Name"].fillna("Unknown")
df["City"] = df["City"].fillna("Unknown")

# 2. Remove duplicates
df = df.drop_duplicates()

# 3. Standardize formatting (e.g., capitalize city names)
df["City"] = df["City"].str.title()

# 4. Optional: Convert data types if necessary
df["Age"] = df["Age"].astype(int)

print("\nCleaned Data:\n", df)
