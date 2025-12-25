# Project Scope

## 1. In Scope
* **Data Processing:** Cleaning and preprocessing of the UCI Online Retail dataset (transaction-level to customer-level).
* **Feature Engineering:** Creation of RFM (Recency, Frequency, Monetary), behavioral, and temporal features.
* **Modeling:** Implementation and comparison of 5 algorithms (Logistic Regression, Decision Tree, Random Forest, XGBoost, Neural Network).
* **Evaluation:** Strict evaluation using a temporal split (Training vs. Observation window).
* **Deployment:** Building a Streamlit web application with Single and Batch prediction capabilities.
* **Documentation:** Technical documentation and business presentation.

## 2. Out of Scope
* **Real-time Inference:** The system will focus on batch predictions, not sub-second real-time processing.
* **Product Recommendations:** The focus is strictly on *retention status*, not specific product up-selling.
* **Inventory Optimization:** Supply chain logistics are excluded.
* **Sentiment Analysis:** No external review or social media data will be used.

## 3. Timeline
* **Total Duration:** 8 Weeks
* **Phase 1-4 (Data Pipeline):** Weeks 1-3
* **Phase 5-7 (Modeling & Eval):** Weeks 4-6
* **Phase 8-10 (Deployment & Docs):** Weeks 7-8

## 4. Constraints
* **Tools:** Must use open-source Python libraries (pandas, scikit-learn, streamlit).
* **Budget:** No paid APIs or cloud services (Deployment via Streamlit Community Cloud).
* **Data:** Limited to the provided historical transactional dataset (no external data enrichment).