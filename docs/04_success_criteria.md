# Success Criteria Matrix

The following thresholds define the success of the machine learning model based on business requirements.

| Metric | Minimum (MVP) | Target | Stretch Goal |
| :--- | :--- | :--- | :--- |
| **ROC-AUC** | 0.75 | 0.80 | 0.85 |
| **Precision** | 0.70 | 0.75 | 0.80 |
| **Recall** | 0.65 | 0.70 | 0.75 |
| **F1-Score** | 0.65 | 0.72 | 0.78 |

## Metric Justification
* **ROC-AUC:** The primary metric as it measures the model's ability to rank customers by risk, regardless of the classification threshold.
* **Precision:** Critical to control the cost of retention campaigns. We do not want to spam loyal customers with discounts.
* **Recall:** Important to ensure we do not miss high-value customers who are actually leaving.