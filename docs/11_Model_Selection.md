# Model Selection Report

## Models Evaluated

| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC | Training Time |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Logistic Regression** | 0.75 | 0.65 | 0.60 | 0.62 | 0.72 | 0.5s |
| **Decision Tree** | 0.72 | 0.60 | 0.58 | 0.59 | 0.68 | 1.2s |
| **Random Forest** | 0.79 | 0.72 | 0.66 | 0.69 | 0.76 | 15.0s |
| **XGBoost** | 0.81 | 0.74 | 0.68 | 0.71 | 0.78 | 8.5s |
| **Neural Network** | **0.82** | **0.75** | **0.69** | **0.72** | **0.79** | 45.0s |

## Selected Model: Neural Network (MLP)
**Justification:**
1.  **Performance:** Achieved the highest ROC-AUC (0.7932), crossing the strict success criteria of 0.75.
2.  **Recall:** Best recall (0.69) among top performers. In churn prediction, catching potential churners (Recall) is slightly more important than precision to prevent revenue loss.

## Metric Prioritization
* **Primary:** **ROC-AUC**. We need a model that ranks risk well across thresholds.
* **Secondary:** **Recall**. Missing a high-value churner (False Negative) costs £500 (LTV), whereas spamming a loyal customer (False Positive) costs only £2 (Marketing cost).

## What I Learned
* **Challenge:** Neural Networks are sensitive to unscaled data.
* **Solution:** Implemented `StandardScaler` in the pipeline specifically to boost NN performance, which raised accuracy by ~10% compared to unscaled data.