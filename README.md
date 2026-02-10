# Explainable AI-Based Intrusion Detection System (XAI-IDS)

## 👨‍🎓 Author
**D Vishnuvardhan Reddy**  
M.Tech CSE (AI & DS)  
KL University  

## 📌 Project Overview
This project implements an Explainable AI based Intrusion Detection System (IDS) using the CICIDS2017 dataset.  
A Random Forest classifier is trained to detect network attacks, and SHAP is used to explain model predictions.

## 🧰 Tech Stack
- Python 3.10
- Pandas, NumPy
- Scikit-learn
- SHAP
- Matplotlib
- Joblib

## 📁 Project Structure
src/
merge_cicids2017.py
preprocess_cicids2017.py
prepare_cicids2017.py
train_rf.py
shap_rf.py


## ⚙️ Workflow
1. Merge CICIDS2017 CSV files  
2. Preprocess data  
3. Train Random Forest classifier  
4. Explain predictions using SHAP  
5. Save model and explanation plots  

## 📊 Results
- Accuracy: ~99.82%
- SHAP used for feature importance and explainability

## 🧪 Dataset
CICIDS2017 (Canadian Institute for Cybersecurity)

## 📜 How to Run
```bash
python src/merge_cicids2017.py
python src/preprocess_cicids2017.py
python src/prepare_cicids2017.py
python src/train_rf.py
python src/shap_rf.py

---

## 🧾 requirements.txt (Optional but Nice)

Create `requirements.txt`:
pandas
numpy
scikit-learn
shap
matplotlib
joblib

---

## 🔗 How to Post on LinkedIn (Exact Steps)

### Step 1: Create GitHub repo (done above)

### Step 2: Post on LinkedIn

Copy this:

> 🚀 Excited to share my latest M.Tech project!  
>  
> 🔐 **Explainable AI-Based Intrusion Detection System (XAI-IDS)**  
>  
> ✅ Built an IDS using Random Forest on CICIDS2017  
> ✅ Achieved 99.8% accuracy  
> ✅ Added explainability using SHAP  
>  
> 📌 Tech: Python, Scikit-learn, SHAP, Pandas  
>  
> 🔗 GitHub: https://github.com/YOUR_USERNAME/xai-ids-cicids2017  
>  
> Thanks to my mentors at KL University 🙌  
>  
> #MachineLearning #CyberSecurity #XAI #MTech #AI #DataScience

---

## ❓Answer to Your Doubt

> ❓ Should I upload all files in src?

### ✅ YES  
These are your **core contribution**  
They prove:
- You wrote code
- You built pipeline
- You trained model
- You used XAI

---

## 🧑‍🏫 To Show Mentor (After CMD Closed)

You can reopen everything anytime:

```bash
E:
cd E:\XAI_IDS_Research
venv\Scripts\activate
python src\train_rf.py
python src\shap_rf.py
