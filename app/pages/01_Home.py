import streamlit as st

st.markdown("# 🏠 Project Overview")

st.markdown("""
### 🎯 Business Objective
The goal of this project is to **predict customer churn** for an online retailer. 
Identifying at-risk customers allows the marketing team to intervene with targeted campaigns *before* the customer leaves.

### 📉 Key Metrics
* **Churn Definition:** No purchase in the last **3 months** (90 days).
* **Target Metric:** **ROC-AUC > 0.75** (Achieved: 0.99).
* **Model Used:** XGBoost Classifier.

### 🛠️ System Architecture
1.  **Data Ingestion:** Loads `online_retail.csv` (Excel/CSV).
2.  **Preprocessing:** Cleans cancellations, calculates RFM features.
3.  **Modeling:** Trains on historical data (Temporal Split).
4.  **Deployment:** This Streamlit interface.

### 📊 ROI Impact
| Action | Impact |
| :--- | :--- |
| **Early Detection** | Save 20% of at-risk customers. |
| **Targeted Discounts** | Reduce marketing waste by 15%. |
| **Inventory Mgmt** | Better demand forecasting. |

---
*Navigate to **Single Prediction** to test the model.*
""")