import streamlit as st

st.markdown("# 📘 Project Documentation")

st.markdown("""
### 1. Project Overview
This project implements an end-to-end **Customer Churn Prediction System** for the E-Commerce sector. It uses historical transaction data to predict the likelihood of a customer stopping their purchasing behavior.

### 2. Model Methodology
* **Algorithm:** XGBoost Classifier (Extreme Gradient Boosting).
* **Training Approach:** Temporal Split (Training on past, validating on future).
* **Target Definition:** "Churn" = No purchase in the observation window (last 3 months).

### 3. Feature Definitions
The model uses the following features to make predictions:

| Feature | Definition | Impact |
| :--- | :--- | :--- |
| **Recency** | Days since the last purchase. | High Recency = **High Risk**. |
| **Frequency** | Total number of distinct orders. | High Frequency = **Low Risk**. |
| **Monetary** | Total lifetime spending (£). | High Monetary = **Low Risk**. |
| **AvgPrice** | Average price per item bought. | Varies by customer segment. |
| **MonetaryPerVisit** | Average spend per order. | Indicates purchasing power. |

### 4. Technical Stack
* **Python 3.9+**
* **Streamlit** (Frontend)
* **XGBoost / Scikit-Learn** (Machine Learning)
* **Pandas / NumPy** (Data Processing)
* **Docker** (Containerization)

### 5. Contact
* **Developer:** Bodepudi Maneesh Koti
* **Project:** Partnr Network Assessment
""")