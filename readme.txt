# ❤️ Heart Disease Prediction System

## 📌 Project Title

**AI-Based Heart Disease Prediction System using Machine Learning**

---

## 📌 Problem Statement

Heart disease is one of the leading causes of death worldwide. Early detection can significantly reduce risk and improve treatment outcomes.
This project aims to build a machine learning model that predicts whether a person is at risk of heart disease based on medical parameters.

---

## ⚙️ Project Pipeline

```
Dataset Collection → Data Cleaning → Feature Engineering
→ Data Splitting → Feature Scaling → Model Training
→ Model Evaluation → Model Selection → Model Saving
→ Streamlit Web App → User Input → Prediction Output
```

---

## 📊 Dataset Details

* **Dataset Name:** Cardiovascular Disease Dataset
* **Source:** Kaggle
* **File Used:** cardio_train.csv

### 🔍 Description:

The dataset contains medical attributes of patients such as:

* Age (in days → converted to years)
* Gender
* Blood Pressure
* Cholesterol Levels
* Heart Rate
* Lifestyle indicators (smoking, alcohol, physical activity)

### 🎯 Target Variable:

* `cardio`

  * 0 → No Heart Disease
  * 1 → Heart Disease

---

## 🤖 Model Details

We implemented multiple Machine Learning algorithms and selected the best-performing model:

### 🔹 Algorithms Used:

* Logistic Regression
* Decision Tree
* Random Forest ⭐ (Best Model)
* K-Nearest Neighbors (KNN)
* Gradient Boosting

### 🧠 Final Model:

**Random Forest Classifier** was selected based on highest accuracy.

### ❗ Note:

This project uses **Machine Learning (ML)**, not Deep Learning, because:

* Dataset is structured (tabular)
* ML models perform better for this type of data
* Faster training and efficient

---

## 🚀 Steps to Run the Project

### 1️⃣ Clone Repository

```
git clone https://github.com/your-username/heart-disease-predictor.git
cd heart-disease-predictor
```

---

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 3️⃣ Run the Application

```
streamlit run app.py
```

---

### 4️⃣ Open in Browser

```
http://localhost:8501
```

---

## 📦 Required Libraries

* streamlit
* numpy
* pandas
* scikit-learn
* pickle
* pillow

---

## 📸 Sample Output

### 🔹 Input Page

Age
Gender
Height / Weight
Blood Pressure
Cholesterol
Sugar
Smoking / Alcohol
Physical Activity


* User enters basic health details

### 🔹 Prediction Result

* ✅ Low Risk
* ❌ High Risk


---

## 👥 Team Members

Gokulnath P
Gopikrishna C
Parthive G
Mohammed Dhanish H
---

## 💡 Future Improvements

* Add Deep Learning model
* Deploy on cloud (Streamlit Cloud / AWS)
* Improve UI/UX design
* Add real-time health data integration

---

## 📌 Conclusion

This system helps in early prediction of heart disease using machine learning, providing a simple and effective decision-support tool for healthcare applications.

---
