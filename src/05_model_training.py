import pandas as pd
import numpy as np
import joblib
import os
import json
import time
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

# Ensure directories exist
os.makedirs('models', exist_ok=True)
os.makedirs('data/processed', exist_ok=True)
os.makedirs('reports/metrics', exist_ok=True)  # Matching your structure for metrics

def load_and_preprocess_data():
    """
    Loads features, performs stratified split, scales data, and saves preprocessor.
    """
    print("Loading feature data...")
    # Load the customer features created in previous step
    df = pd.read_csv('data/processed/customer_features.csv')
    
    # Drop identifiers and Target
    X = df.drop(columns=['CustomerID', 'Churn'])
    y = df['Churn']
    
    # 1. Handle Categorical Encoding (One-Hot)
    # Identify categorical columns (object/category)
    categorical_cols = X.select_dtypes(include=['object', 'category']).columns
    print(f"Encoding categorical columns: {list(categorical_cols)}")
    X = pd.get_dummies(X, columns=categorical_cols, drop_first=True)
    
    # Save feature names order for inference API (Crucial for deployment)
    feature_names = list(X.columns)
    with open('data/processed/feature_names.json', 'w') as f:
        json.dump(feature_names, f)
        
    # 2. Stratified Split
    # Split: 70% Train, 15% Val, 15% Test
    # First: Split off Test (15%)
    X_temp, X_test, y_temp, y_test = train_test_split(
        X, y, test_size=0.15, stratify=y, random_state=42
    )
    # Second: Split remaining 85% into Train (70% total) and Val (15% total)
    # 0.15 / 0.85 ≈ 0.1765
    X_train, X_val, y_train, y_val = train_test_split(
        X_temp, y_temp, test_size=0.1765, stratify=y_temp, random_state=42
    )
    
    # 3. Scaling (Numerical only)
    # PDF Requirement: Scale features [cite: 1754]
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_val_scaled = scaler.transform(X_val)
    X_test_scaled = scaler.transform(X_test)
    
    # Save Preprocessor (Scaler) as 'preprocessor.pkl' to match your tree
    joblib.dump(scaler, 'models/preprocessor.pkl')
    print("Saved scaler to models/preprocessor.pkl")
    
    # Save split data for evaluation scripts if needed
    pd.DataFrame(X_train_scaled, columns=feature_names).to_csv('data/processed/X_train.csv', index=False)
    pd.DataFrame(X_val_scaled, columns=feature_names).to_csv('data/processed/X_val.csv', index=False)
    pd.DataFrame(X_test_scaled, columns=feature_names).to_csv('data/processed/X_test.csv', index=False)
    y_train.to_csv('data/processed/y_train.csv', index=False)
    y_val.to_csv('data/processed/y_val.csv', index=False)
    y_test.to_csv('data/processed/y_test.csv', index=False)

    return X_train_scaled, y_train, X_val_scaled, y_val

def train_models():
    X_train, y_train, X_val, y_val = load_and_preprocess_data()
    
    # Define the 5 models explicitly required by PDF [cite: 397-401]
    models = {
        "Logistic Regression": LogisticRegression(random_state=42, max_iter=1000),
        "Decision Tree": DecisionTreeClassifier(random_state=42, max_depth=10),
        "Random Forest": RandomForestClassifier(random_state=42, n_estimators=100),
        "XGBoost": XGBClassifier(random_state=42, use_label_encoder=False, eval_metric='logloss'),
        "Neural Network": MLPClassifier(random_state=42, max_iter=1000, hidden_layer_sizes=(100, 50))
    }

    # Map to EXACT filenames from your file structure
    filename_map = {
        "Logistic Regression": "logreg_model.pkl",
        "Decision Tree": "decision_tree_model.pkl",
        "Random Forest": "random_forest_model.pkl",
        "XGBoost": "xgboost_model.pkl",
        "Neural Network": "neural_network_model.pkl"
    }

    results = []
    best_roc_auc = 0
    best_model_name = ""

    print("\n--- Starting Training for All 5 Models ---")

    for name, model in models.items():
        print(f"Training {name}...")
        start_time = time.time()
        
        # Train
        model.fit(X_train, y_train)
        
        # Predict on Validation
        y_pred = model.predict(X_val)
        
        # Handle probability for ROC-AUC
        if hasattr(model, "predict_proba"):
            y_prob = model.predict_proba(X_val)[:, 1]
        else:
            y_prob = y_pred
        
        train_time = time.time() - start_time
        
        # Calculate Metrics
        roc = roc_auc_score(y_val, y_prob)
        metrics = {
            "Model": name,
            "Accuracy": accuracy_score(y_val, y_pred),
            "Precision": precision_score(y_val, y_pred),
            "Recall": recall_score(y_val, y_pred),
            "F1-Score": f1_score(y_val, y_pred),
            "ROC-AUC": roc,
            "Training Time": round(train_time, 4)
        }
        results.append(metrics)
        
        # SAVE INDIVIDUAL MODEL [cite: 1968]
        save_path = f"models/{filename_map[name]}"
        joblib.dump(model, save_path)
        print(f"  -> Saved {name} to {save_path}")

        # Check for Best Model
        if roc > best_roc_auc:
            best_roc_auc = roc
            best_model_name = name
            # Save Best Model [cite: 402]
            joblib.dump(model, 'models/best_model.pkl')

    # Save comparison to CSV [cite: 1955]
    results_df = pd.DataFrame(results)
    results_df.to_csv('models/model_comparison.csv', index=False)
    
    # Save best metrics for submission.json population
    best_metrics = results_df[results_df['Model'] == best_model_name].iloc[0].to_dict()
    with open('models/best_model_metrics.json', 'w') as f:
        json.dump(best_metrics, f, indent=4)

    print("\n--- Training Complete ---")
    print(f"Champion Model: {best_model_name} (ROC-AUC: {best_roc_auc:.4f})")
    print("Saved as 'models/best_model.pkl'")

if __name__ == "__main__":
    train_models()