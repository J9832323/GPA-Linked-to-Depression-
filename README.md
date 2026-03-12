# GPA-Linked-to-Depression

Exploring the relationship between academic performance and depression indicators in college students — using Python to identify whether GPA and lifestyle factors can signal mental health risk.

## 📊 Project Overview

This project investigates whether a measurable relationship exists between GPA and self-reported depression symptoms using college student survey data. The findings have real-world implications for university wellness programs and early intervention strategies.

The analysis is divided into two primary phases:

**Exploratory Data Analysis:** Investigating distributions, correlations, and patterns between GPA ranges and depression indicators including sleep, social activity, and academic load.

**Classification Modeling:** Applying machine learning to predict depression risk categories based on student attributes, and evaluating which features carry the most predictive weight.

## 🛠️ Tech Stack

**Language:** Python

**Modeling:** scikit-learn

**Data Manipulation:** Pandas, NumPy

**Visualization:** Matplotlib, Seaborn

## 🔍 Key Methodologies

### 1. Exploratory Data Analysis (EDA)
Distributions and correlations were mapped across GPA ranges and depression indicators. Key questions explored: Do lower GPA students report higher depression rates? Which lifestyle factors (sleep, social activity, academic load) correlate most strongly with mental health outcomes?

### 2. Data Cleaning & Preprocessing
Missing values were handled, categorical variables standardized, and features prepared for classification modeling.

### 3. Classification Modeling
Machine learning was applied to predict depression risk categories from student attributes. Feature importance was evaluated to identify the strongest predictors across academic and lifestyle variables.

### 4. Visualization
Charts were built to communicate the relationship between GPA and mental health outcomes clearly — designed to be readable by a non-technical audience.

## 📈 Key Questions Explored

- Do students with lower GPAs report higher rates of depression symptoms?
- Which features (sleep, social activity, academic load) correlate most strongly with depression indicators?
- Can a predictive model identify at-risk students based on academic and lifestyle data?

## 🚀 How to Run

Clone the repository.

Install dependencies:
```bash
pip install pandas numpy scikit-learn matplotlib seaborn
```

Open and run `GPA_Depression_Analysis.ipynb` in Jupyter Notebook to reproduce the full analysis.

---

*Note: This project is for academic and analytical purposes only. All data is anonymized survey data. The goal is to surface patterns that could inform student wellness resources — not to make clinical determinations.*
