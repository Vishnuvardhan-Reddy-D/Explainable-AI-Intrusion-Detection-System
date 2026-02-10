import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib
import os

DATA_DIR = r"E:\XAI_IDS_Research\data\CICIDS2017\processed"
MODEL_DIR = r"E:\XAI_IDS_Research\models"

os.makedirs(MODEL_DIR, exist_ok=True)

print("📥 Loading train/test data...")
X_train = pd.read_csv(os.path.join(DATA_DIR, "X_train.csv"))
X_test = pd.read_csv(os.path.join(DATA_DIR, "X_test.csv"))
y_train = pd.read_csv(os.path.join(DATA_DIR, "y_train.csv")).values.ravel()
y_test = pd.read_csv(os.path.join(DATA_DIR, "y_test.csv")).values.ravel()

print("🚀 Training Random Forest model...")
rf = RandomForestClassifier(
    n_estimators=100,
    n_jobs=-1,
    random_state=42
)

rf.fit(X_train, y_train)

print("🧪 Evaluating model...")
y_pred = rf.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Save model
model_path = os.path.join(MODEL_DIR, "rf_cicids2017.pkl")
joblib.dump(rf, model_path)

print("✅ Model saved at:", model_path)
