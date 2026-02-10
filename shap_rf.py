import os
import joblib
import pandas as pd
import shap
import matplotlib.pyplot as plt

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data", "CICIDS2017", "processed")
MODEL_DIR = os.path.join(BASE_DIR, "models")

# Load data
print("📥 Loading data...")
X_train = pd.read_csv(os.path.join(DATA_DIR, "X_train.csv"))

# Take a small sample (SHAP is expensive)
X_sample = X_train.sample(1000, random_state=42)

# Load model
print("📦 Loading Random Forest model...")
model = joblib.load(os.path.join(MODEL_DIR, "rf_cicids2017.pkl"))

# SHAP explainer
print("🧠 Computing SHAP values...")
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_sample)

# Plot
print("📊 Generating SHAP summary plot...")
shap.summary_plot(shap_values, X_sample, show=False)

# Save plot
output_path = os.path.join(MODEL_DIR, "shap_summary_rf.png")
plt.savefig(output_path, bbox_inches="tight")
plt.close()

print(f"✅ SHAP plot saved at: {output_path}")
