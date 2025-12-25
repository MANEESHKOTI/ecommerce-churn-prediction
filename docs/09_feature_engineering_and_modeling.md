# Feature Engineering & Model Selection

## Part 1: Feature Dictionary

### Target Variable
* **Churn (Binary):** 1 = Churned (No purchase in last 3 months), 0 = Active.

### RFM Features (Recency, Frequency, Monetary)
| Feature | Type | Description | Business Meaning |
| :--- | :--- | :--- | :--- |
| **Recency** | Integer | Days since last purchase in Training Period. | Lower = More active, less likely to churn. |
| **Frequency** | Integer | Total number of unique invoices. | Higher = Loyal customer. |
| **TotalSpent** | Float | Total lifetime spend (£). | High value customers we must retain. |
| **AvgOrderValue**| Float | Average spend per transaction. | Indicates spending power. |

### Behavioral & Temporal Features
| Feature | Type | Description | Business Meaning |
| :--- | :--- | :--- | :--- |
| **AvgDaysBetween**| Float | Avg days between consecutive orders. | Consistency of purchasing habits. |
| **ProdDiversity** | Float | Ratio of unique products to total items. | Variety seeker vs. bulk buyer. |
| **Returns** | Integer | Number of return transactions. | Dissatisfaction indicator. |
| **Seasonality** | Float | Spending variance across months. | Seasonal vs. regular shopper. |

---

## Part 2: Model Selection Report

### Models Evaluated
We trained and compared 5 algorithms. Below are the performance metrics on the Validation Set:

| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Logistic Regression** | 0.75 | 0.65 | 0.60 | 0.62 | 0.72 |
| **Decision Tree** | 0.72 | 0.60 | 0.58 | 0.59 | 0.68 |
| **Random Forest** | 0.79 | 0.72 | 0.66 | 0.69 | 0.76 |
| **XGBoost** | 0.81 | 0.74 | 0.68 | 0.71 | 0.78 |
| **Neural Network** | **0.82** | **0.75** | **0.69** | **0.72** | **0.7932** |

### Selected Model: Neural Network (MLP)
* **Justification:** The Neural Network achieved the highest **ROC-AUC (0.7932)**, successfully crossing the project's target threshold of 0.75. It provided the best balance between Precision and Recall.
* **Metric Prioritization:** We prioritized **ROC-AUC** and **Recall** because missing a churner (False Negative) is more costly to the business (lost LTV) than offering a discount to a loyal user (False Positive).

### Hyperparameters
* **Hidden Layers:** (100, 50)
* **Activation:** ReLU
* **Solver:** Adam
* **Scaling:** Standard Scaling (Critical for Neural Net performance).