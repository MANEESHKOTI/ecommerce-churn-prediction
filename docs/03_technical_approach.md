# Technical Approach

## 1. Problem Type: Binary Classification
We frame this as a supervised binary classification problem because the output is categorical: a customer will either Churn (1) or Stay (0) within the defined observation window. Regression is not suitable as we are predicting a state, not a continuous value (like future spend).

## 2. Feature Engineering Strategy
Since the raw data is transactional (one row per item purchased), we must aggregate it to the **Customer Level**.
* **RFM Analysis:** Recency, Frequency, and Monetary value are proven predictors of customer lifetime value.
* **Behavioral Features:** Average days between purchases, basket size, and return rates.
* **Temporal Features:** Purchase velocity and activity in specific windows (last 30/60/90 days).

## 3. Modeling Strategy
We will implement and compare 5 distinct algorithms to find the best balance of bias and variance:
1.  **Logistic Regression:** As a linear baseline for interpretability.
2.  **Decision Tree:** To capture non-linear patterns.
3.  **Random Forest:** To reduce overfitting via bagging.
4.  **XGBoost (Gradient Boosting):** For high predictive performance on tabular data.
5.  **Neural Network (MLP):** To capture complex, high-dimensional interactions.

## 4. Deployment Strategy
The final model will be serialized (pickled) and wrapped in a Python API. A Streamlit frontend will consume this API to provide an interactive interface for stakeholders to upload customer data and receive churn probabilities.