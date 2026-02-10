import os
import pandas as pd

# Correct path where CSV files actually exist
DATA_DIR = r"E:\XAI_IDS_Research\data\CICIDS2017\raw\MachineLearningCSV\MachineLearningCVE"
OUTPUT_DIR = r"E:\XAI_IDS_Research\data\CICIDS2017\processed"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "cicids2017_merged.csv")

os.makedirs(OUTPUT_DIR, exist_ok=True)

csv_files = [f for f in os.listdir(DATA_DIR) if f.endswith(".csv")]
print("CSV files found:", csv_files)

dfs = []
for file in csv_files:
    file_path = os.path.join(DATA_DIR, file)
    print(f"Reading {file} ...")
    df = pd.read_csv(file_path)
    dfs.append(df)

combined_df = pd.concat(dfs, ignore_index=True)
combined_df.to_csv(OUTPUT_FILE, index=False)

print("✅ Merged dataset saved at:", OUTPUT_FILE)
print("Final shape:", combined_df.shape)
