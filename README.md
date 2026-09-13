# 🩺 Diabetes Prediction using AI

## 📌 Project Overview

Diabetes Prediction using AI is an Artificial Intelligence project
that predicts the likelihood of diabetes based on patient health information.

The project uses a **Decision Tree Classifier** trained on the
**Pima Indians Diabetes Dataset**.

A user can enter patient information through a simple **Streamlit web
application**, and the trained Machine Learning model provides a prediction
along with an estimated diabetes probability.

---

## 🎯 Objectives

The main objectives of this project are:

- To understand the basics of Machine Learning.
- To preprocess and clean healthcare data.
- To train multiple Machine Learning classification models.
- To compare model performance.
- To select the best-performing model.
- To deploy the model as a web application using Streamlit.
- To provide an easy-to-use interface for diabetes prediction.

---

## 🧠 Machine Learning Models

The following classification algorithms were trained and compared:

1. Logistic Regression
2. Decision Tree
3. Random Forest
4. K-Nearest Neighbors (KNN)

After comparing their performance, the **Decision Tree Classifier** was selected
as the final model for deployment.

---

## 📈 Model Performance

Four Machine Learning classification models were trained and evaluated
on the diabetes dataset.

| Model | Accuracy |
|---|---:|
| Logistic Regression | 67.53% |
| Decision Tree | 72.08% |
| Random Forest | 70.78% |
| KNN | 72.08% |

### 🏆 Selected Model

**Decision Tree Classifier** was selected for deployment in the Streamlit
web application.

The Decision Tree and KNN models achieved the highest accuracy of
**72.08%** among the tested models. The Decision Tree was selected as
the final deployed model for this project.
---

## 📊 Dataset

The project uses the **Pima Indians Diabetes Dataset**.

The dataset contains medical and demographic information such as:

- Pregnancies
- Glucose
- Blood Pressure
- Skin Thickness
- Insulin
- BMI
- Diabetes Pedigree Function
- Age

### Target Variable

`Outcome`

- `0` → Lower likelihood of diabetes
- `1` → Higher likelihood of diabetes

---

## 🔄 Project Workflow

```text
Dataset
   ↓
Data Loading
   ↓
Data Cleaning
   ↓
Exploratory Data Analysis
   ↓
Train-Test Split
   ↓
Model Training
   ↓
Model Comparison
   ↓
Decision Tree Selection
   ↓
Model Saving
   ↓
Streamlit Web Application
   ↓
Diabetes Prediction
