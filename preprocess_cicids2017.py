import pandas as pd
import numpy as np
import os

# Paths
INPUT_FILE = r"E:\XAI_IDS_Research\data\CICIDS2017\processed\cicids2017_merged.csv"
OUTPUT_FILE = r"E:\XAI_IDS_Research\data\CICIDS2017\processed\cicids2017_clean.csv"

print("📥 Loading dataset...")
df = pd.read_csv(INPUT_FILE)

print("Initial shape:", df.shape)

# Replace infinite values with NaN
df.replace([np.inf, -np.inf], np.nan, inplace=True)

# Drop rows with NaN
df.dropna(inplace=True)

print("After removing NaN/Inf:", df.shape)

# Remove duplicate rows
df.drop_duplicates(inplace=True)

print("After removing duplicates:", df.shape)

# Strip column names
df.columns = df.columns.str.strip()

# Save cleaned dataset
df.to_csv(OUTPUT_FILE, index=False)

print("✅ Cleaned dataset saved at:")
print(OUTPUT_FILE)
