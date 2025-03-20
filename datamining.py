import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skew

# Load dataset
file_path = "data.csv"
df = pd.read_csv(file_path)

# Convert 'Minute' to numeric (handle extra characters like '90+5')
def convert_minute(value):
    try:
        if '+' in str(value):  # Handle extra time (e.g., "90+5")
            base, extra = value.split('+')
            return int(base) + int(extra)
        return int(value)
    except:
        return np.nan  # Handle missing or non-numeric values

df['Minute'] = df['Minute'].apply(convert_minute).dropna()

# Descriptive Statistics
mean = df['Minute'].mean()
median = df['Minute'].median()
mode = df['Minute'].mode()[0]
variance = df['Minute'].var()
std_dev = df['Minute'].std()
data_range = df['Minute'].max() - df['Minute'].min()

# Print statistics
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")
print(f"Variance: {variance}")
print(f"Standard Deviation: {std_dev}")
print(f"Range: {data_range}")

# Check skewness
skewness = skew(df['Minute'].dropna())
print(f"Skewness: {skewness}")

# Determine distribution type
if skewness > 0:
    distribution = "Positively Skewed (Right-Skewed)"
elif skewness < 0:
    distribution = "Negatively Skewed (Left-Skewed)"
else:
    distribution = "Approximately Normal"

print(f"Distribution Type: {distribution}")

# Plot Histogram
plt.hist(df['Minute'].dropna(), bins=10, edgecolor='black')
plt.title('Jumlah Pembagian Gol Karir Ronaldo')
plt.xlabel('Minute')
plt.ylabel('Frequency')
plt.show()
