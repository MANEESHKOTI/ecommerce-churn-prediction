# Churn Definition Strategy

## 1. Methodology: Observation Window
We use a **Temporal Split** approach to define churn, avoiding data leakage by strictly separating the timeline.

### Time Windows
* **Training Period:** `2009-12-01` to `2011-09-09` (First 21 months)
    * *Purpose:* Used to calculate features (RFM, History).
* **Observation Period:** `2011-09-10` to `2011-12-09` (Last 3 months)
    * *Purpose:* Used strictly to label the target variable (Churn Yes/No).

## 2. Definition Logic
* **Active Customer:** A customer who made **at least one purchase** during the **Observation Period**.
* **Churned Customer:** A customer who existed in the Training Period but made **zero purchases** during the **Observation Period**.

## 3. Justification
* **Why 3 Months?** In non-subscription retail, a 90-day purchase cycle is the industry standard for defining dormancy.
* **Churn Rate Check:** This definition resulted in a churn rate of approximately **20-40%**, which falls within the expected range for this dataset.

## 4. Feature Safety (No Leakage)
All features (Recency, Frequency, Monetary) are calculated using **ONLY** data from the **Training Period**. No future data from the Observation Period is used for feature generation.