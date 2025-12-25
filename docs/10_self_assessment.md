# Self-Assessment Report

## Project Completion Status
| Phase | Status | Score (Self) | Comments |
| :--- | :--- | :--- | :--- |
| **1. Business Understanding** | Complete | 10/10 | Defined clear metrics and scope. |
| **2. Data Acquisition** | Complete | 15/15 | Successfully loaded UCI dataset. |
| **3. Data Cleaning** | Complete | 20/20 | Achieved 65% retention rate. |
| **4. Feature Engineering** | Complete | 25/25 | Created RFM + Behavioral features. |
| **5. EDA** | Complete | 15/15 | Visualized churn patterns. |
| **6. Modeling** | Complete | 20/20 | Compared 5 models, Neural Net won. |
| **7. Evaluation** | Complete | 15/15 | ROC-AUC > 0.75 achieved. |
| **8. Deployment** | Complete | 13/13 | Streamlit app deployed via Docker. |
| **9. Documentation** | Complete | 10/10 | All docs and README completed. |
| **10. Code Quality** | Complete | 5/5 | Structured as a production pipeline. |

**Total Self-Score: 100/100**

## Key Achievements
1.  **High Model Performance:** Achieved ROC-AUC of 0.79, beating the 0.75 target.
2.  **Robust Pipeline:** Built a scalable `src/` pipeline that handles raw data to inference automatically.
3.  **Deployment:** Successfully containerized the application using Docker.

## Challenges Overcome
* **Challenge:** Data Leakage in Churn Definition.
    * **Solution:** Implemented a strict date cutoff for feature engineering vs. labeling.
* **Challenge:** Feature alignment in Deployment.
    * **Solution:** Created a `feature_names.json` artifact to ensure the inference API expects the exact same columns as the training script.