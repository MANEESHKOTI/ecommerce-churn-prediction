# PROJECT PRESENTATION: Customer Churn Prediction
**Global Placement Program - Evaluation Deliverable**

---

## 1. Business Problem & Scope
* **Objective:** Build an end-to-end pipeline to predict customer churn.
* **Scope:** From raw data acquisition to a production-ready Streamlit deployment.
* **Stakeholders:** Marketing and Retention teams.

## 2. Data Pipeline & Quality
* **Acquisition:** Automated scripts for data ingestion.
* **Cleaning:** Robust handling of nulls and type-casting (documented in `07_data_cleaning_report.md`).
* **Validation:** JSON-based validation reports ensure data integrity for the evaluator.

## 3. The Solution (Deployment)
* **Streamlit App:** Features single/batch prediction and an interactive dashboard.
* **Containerization:** Fully Dockerized using `docker-compose` for "one-click" evaluation.
* **Reproducibility:** Versioned JSON artifacts track feature info and model stats.

## 4. Key Results
* **Recall:** Focused on capturing the maximum number of true churners.
* **Insights:** Identified [Key Feature, e.g., Contract Type] as the primary driver of churn.

---
*Note: Full documentation available in the /docs folder.*