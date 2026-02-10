# Explainable AI-Based Intrusion Detection System (XAI-IDS)

## 👨‍🎓 Author
**D Vishnuvardhan Reddy**  
M.Tech CSE (AI & DS)  
KL University  
# Explainable AI for Intrusion Detection Systems (XAI-IDS)

This project implements an Explainable AI (XAI) based Intrusion Detection System using the CICIDS2017 dataset.
A Random Forest classifier is trained to detect different types of network attacks, and SHAP is used to explain
model predictions for transparency and trust.

## 🚀 Features
- Data preprocessing & preparation (CICIDS2017)
- Random Forest classifier for intrusion detection
- High accuracy multi-class classification
- SHAP-based explainability for feature importance
- Reproducible training and evaluation pipeline

## 🛠️ Tech Stack
- Python 3.10
- NumPy, Pandas, Scikit-learn
- SHAP
- Matplotlib

## 📂 Project Structure
XAI-IDS-Project/
├── src/ # Source code
├── results/ # Output plots (SHAP)
├── notebooks/ # (Optional)
├── README.md
├── requirements.txt
└── .gitignore

## ▶️ How to Run
```bash
# Activate virtual environment
venv\Scripts\activate

# Prepare dataset
python src\prepare_cicids2017.py

# Train model
python src\train_rf.py

# Generate SHAP explanations
python src\shap_rf.py

📊 Results

Accuracy: ~99.8% on CICIDS2017

SHAP summary plot shows top features contributing to intrusion detection.

📌 Dataset

CICIDS2017 dataset (not uploaded due to size limits).
Download from: https://www.unb.ca/cic/datasets/ids-2017.html

