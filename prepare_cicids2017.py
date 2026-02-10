import os
import pandas as pd
from sklearn.model_selection import train_test_split

# Paths
DATA_DIR = r"E:\XAI_IDS_Research\data\CICIDS2017\processed"
INPUT_FILE = os.path.join(DATA_DIR, "cicids2017_clean.csv")

# Output files
X_TRAIN = os.path.join(DATA_DIR, "X_train.csv")
X_TEST  = os.path.join(DATA_DIR, "X_test.csv")
Y_TRAIN = os.path.join(DATA_DIR, "y_train.csv")
Y_TEST  = os.path.join(DATA_DIR, "y_test.csv")

print("📥 Loading cleaned dataset...")
df = pd.read_csv(INPUT_FILE)

print("Dataset shape:", df.shape)

# Label column
LABEL_COL = "Label"

# Features & target
X = df.drop(columns=[LABEL_COL])
y = df[LABEL_COL]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print("Train shape:", X_train.shape)
print("Test shape:", X_test.shape)

# Save files
X_train.to_csv(X_TRAIN, index=False)
X_test.to_csv(X_TEST, index=False)
y_train.to_csv(Y_TRAIN, index=False)
y_test.to_csv(Y_TEST, index=False)

print("✅ Train/test datasets saved successfully")
