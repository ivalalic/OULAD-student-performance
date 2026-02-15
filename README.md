# OULAD Student Performance Prediction

This project analyzes the **OULAD dataset (Open University Learning Analytics Dataset)** and builds a machine learning model to predict student performance.

The dataset was obtained from Kaggle.

---

## Project Overview

The project demonstrates a complete machine learning workflow:

* data preprocessing
* feature engineering
* model training and evaluation
* model selection
* deployment using FastAPI
* dashboard visualization in Tableau

---

## Dataset

Dataset: **OULAD (Open University Learning Analytics Dataset)**
Source: Kaggle

The dataset contains student demographic information, course engagement data, and assessment results.

---

## Machine Learning Workflow

The Jupyter notebook contains the full step-by-step process:

### 1. Data loading

Multiple OULAD tables were loaded and merged.

### 2. Data preprocessing

* handling missing values
* encoding categorical variables
* scaling numeric features

### 3. Feature engineering

Derived features related to:

* engagement
* academic performance
* course participation

### 4. Model training

The following models were compared:

* Logistic Regression
* Random Forest
* Neural Network

### 5. Model evaluation

Models were evaluated using:

* accuracy
* ROC-AUC
* classification metrics

The best model was selected and saved.

---

## Model Deployment

The trained pipeline was saved as:

```
final_oulad_pipeline.joblib
```

A simple FastAPI service was implemented to serve predictions.

Run API:

```
uvicorn api.app:app --reload
```

Example request:

```
POST /predict
Content-Type: application/json

{
  "region": "East Anglian Region",
  "highest_education": "A Level or Equivalent",
  "imd_band": "40-50",
  "age_band": "0-35",
  "num_of_prev_attempts": 0,
  "studied_credits": 60,
  "disabled": 0,
  "female": 1
}
```

Returns:

* probability
* prediction

---

## Dashboard

A Tableau dashboard was created to visualize:

* student engagement
* performance KPIs
* module statistics

File:

```
tableau/OULADTableau.twbx
```

---

## Technologies Used

Python
pandas
scikit-learn
FastAPI
Tableau
Git

---

## Author

Iva Lalić
