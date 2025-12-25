# Technical Documentation

## 1. System Architecture
The project follows a modular pipeline architecture:
`Raw Data` -> `src/01_acquisition` -> `src/02_cleaning` -> `src/03_features` -> `src/05_training` -> `Models` -> `App`

## 2. Data Pipeline
* **01_data_acquisition.py:** Downloads UCI dataset.
* **02_data_cleaning.py:** Removes null IDs, cancellations, and outliers. Saves `cleaned_transactions.csv`.
* **03_feature_engineering.py:**
    * Splits data by time (Training < 2011-09-09 < Observation).
    * Aggregates transactions to Customer Level.
    * Saves `customer_features.csv`.

## 3. Model Architecture (Neural Network)
* **Library:** `sklearn.neural_network.MLPClassifier`
* **Layers:** Input (30) -> Hidden (100, ReLU) -> Hidden (50, ReLU) -> Output (1, Sigmoid)
* **Solver:** Adam
* **Preprocessing:** Standard Scaling (Required).

## 4. Deployment Architecture
* **Container:** Docker (Python 3.9-slim).
* **Frontend:** Streamlit.
* **Inference:** `src/inference_api.py` loads `best_model.pkl` and `preprocessor.pkl` to make real-time predictions.

## 5. Troubleshooting
* **Issue:** `FileNotFoundError` for models.
    * *Fix:* Run `python src/05_model_training.py` to regenerate artifacts.
* **Issue:** Docker permission denied.
    * *Fix:* Ensure `run.sh` is executable or run with `sudo`.