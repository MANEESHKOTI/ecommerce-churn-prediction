# E-Commerce Customer Churn Prediction

## Project Overview
This project is an end-to-end machine learning solution designed to predict customer churn for an e-commerce platform. Using historical transactional data, we built a pipeline that transforms raw logs into customer-level insights, engineering features based on RFM (Recency, Frequency, Monetary) analysis. The final model identifies customers at risk of leaving, enabling targeted retention campaigns.

## Business Problem
**Goal:** Predict customers who will not make a purchase in the next 90 days.
* **Context:** Customer acquisition costs are 5-25x higher than retention.
* **Impact:** Reducing churn by 15-20% can significantly increase customer lifetime value (LTV).
* **Success Metric:** ROC-AUC > 0.75 on the test set.

## Dataset
* **Source:** UCI Machine Learning Repository (Online Retail II).
* **Size:** ~541,909 rows (Raw), ~350,000 rows (Cleaned).
* **Period:** Dec 2009 - Dec 2011.

## Methodology
1.  **Data Cleaning:** Removed missing CustomerIDs, cancellations, and outliers (IQR).
2.  **Feature Engineering:** Created 30+ features including RFM scores, purchase velocity, and seasonality.
3.  **Modeling:** Trained 5 algorithms (LogReg, Decision Tree, Random Forest, XGBoost, Neural Network).
4.  **Final Model:** **Neural Network (MLP)** selected for highest ROC-AUC (0.7932).

## Installation & Usage

### 1. Clone Repository
```bash
git clone [https://github.com/MANEESHKOTI/ecommerce-churn-prediction.git](https://github.com/MANEESHKOTI/ecommerce-churn-prediction.git)
cd ecommerce-churn-prediction