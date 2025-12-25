# Business Problem Statement

## 1. Business Context
RetailCo Analytics operates in the competitive e-commerce sector where customer acquisition costs are rising (typically 5-25x more expensive than retention). The company currently lacks a data-driven method to identify customers at risk of leaving. Retention is critical for maximizing Customer Lifetime Value (CLV) and sustaining revenue growth.

## 2. Problem Definition
The objective is to predict customer churn using historical transactional data.
* **Churn Definition:** A customer is considered "churned" if they have not made a valid purchase in the last **90 days (3 months)**.
* **Target Variable:** Binary classification (1 = Churned, 0 = Active).

## 3. Stakeholders
* **Marketing Team:** Needs specific customer segments (e.g., "At Risk", "Champions") to target with personalized retention campaigns.
* **Sales Team:** Requires lists of high-value churn-risk customers for direct outreach.
* **Product Team:** Needs insights into which products or behaviors drive loyalty versus churn.
* **Executive Team:** Focused on the ROI of retention efforts and overall churn rate reduction.

## 4. Business Impact
Successful implementation of this model is expected to:
* **Reduce Churn Rate:** Target reduction of 15-20% within the first year.
* **Increase Revenue:** By retaining high-value customers who would otherwise leave.
* **Optimize Budget:** Cost savings by focusing marketing spend only on at-risk customers rather than generic blasting.

## 5. Success Metrics
* **Primary Metric:** **ROC-AUC Score > 0.78** (Indicates strong ability to distinguish between churners and active users).
* **Secondary Metrics:**
    * **Precision > 0.75:** To minimize false positives (wasting money on customers who weren't going to leave).
    * **Recall > 0.70:** To ensure we catch the majority of actual churners.
    * **F1-Score > 0.72:** A balance between precision and recall.