import pandas as pd
import numpy as np
import joblib
import os
import json
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score, roc_auc_score,
    confusion_matrix, roc_curve, precision_recall_curve, brier_score_loss
)
from sklearn.calibration import calibration_curve

# Define paths based on your structure
DATA_PATH = 'data/processed'
MODELS_PATH = 'models'
REPORTS_FIG_PATH = 'reports/figures'
REPORTS_METRICS_PATH = 'reports/metrics'

# Ensure output directories exist
os.makedirs(REPORTS_FIG_PATH, exist_ok=True)
os.makedirs(REPORTS_METRICS_PATH, exist_ok=True)

def load_test_data():
    print("Loading Test Data...")
    X_test = pd.read_csv(f'{DATA_PATH}/X_test.csv')
    y_test = pd.read_csv(f'{DATA_PATH}/y_test.csv').values.ravel()
    return X_test, y_test

def load_model():
    print("Loading Champion Model...")
    model = joblib.load(f'{MODELS_PATH}/best_model.pkl')
    return model

def plot_confusion_matrix(y_true, y_pred, save_path):
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False)
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.title('Confusion Matrix (Test Set)')
    plt.savefig(save_path)
    plt.close()
    print(f"Saved Confusion Matrix to {save_path}")

def plot_roc_curve(y_true, y_prob, roc_auc, save_path):
    fpr, tpr, _ = roc_curve(y_true, y_prob)
    plt.figure(figsize=(8, 6))
    plt.plot(fpr, tpr, label=f'AUC = {roc_auc:.4f}')
    plt.plot([0, 1], [0, 1], 'k--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curve')
    plt.legend(loc='lower right')
    plt.savefig(save_path)
    plt.close()
    print(f"Saved ROC Curve to {save_path}")

def plot_precision_recall_curve(y_true, y_prob, save_path):
    precision, recall, _ = precision_recall_curve(y_true, y_prob)
    plt.figure(figsize=(8, 6))
    plt.plot(recall, precision)
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.title('Precision-Recall Curve')
    plt.savefig(save_path)
    plt.close()
    print(f"Saved Precision-Recall Curve to {save_path}")

def plot_prediction_distribution(y_prob, y_true, save_path):
    plt.figure(figsize=(10, 6))
    sns.histplot(y_prob[y_true == 0], color='blue', label='Active', kde=True, stat="density", alpha=0.5)
    sns.histplot(y_prob[y_true == 1], color='red', label='Churned', kde=True, stat="density", alpha=0.5)
    plt.xlabel('Predicted Probability of Churn')
    plt.title('Prediction Distribution by Class')
    plt.legend()
    plt.savefig(save_path)
    plt.close()
    print(f"Saved Prediction Distribution to {save_path}")

def plot_calibration_curve(y_true, y_prob, save_path):
    prob_true, prob_pred = calibration_curve(y_true, y_prob, n_bins=10)
    plt.figure(figsize=(8, 6))
    plt.plot(prob_pred, prob_true, marker='o', label='Model')
    plt.plot([0, 1], [0, 1], 'k--', label='Perfectly Calibrated')
    plt.xlabel('Mean Predicted Probability')
    plt.ylabel('Fraction of Positives')
    plt.title('Calibration Curve')
    plt.legend()
    plt.savefig(save_path)
    plt.close()
    print(f"Saved Calibration Curve to {save_path}")

def evaluate_model():
    X_test, y_test = load_test_data()
    model = load_model()

    # Predictions
    print("Generating predictions...")
    y_pred = model.predict(X_test)
    
    # Check if model supports predict_proba (Neural Networks and most classifiers do)
    if hasattr(model, "predict_proba"):
        y_prob = model.predict_proba(X_test)[:, 1]
    else:
        # Fallback for models without predict_proba (unlikely for your list)
        y_prob = y_pred 

    # --- Metrics Calculation ---
    metrics = {
        "accuracy": accuracy_score(y_test, y_pred),
        "precision": precision_score(y_test, y_pred),
        "recall": recall_score(y_test, y_pred),
        "f1_score": f1_score(y_test, y_pred),
        "roc_auc": roc_auc_score(y_test, y_prob)
    }

    print("\n--- Test Set Metrics ---")
    for k, v in metrics.items():
        print(f"{k.capitalize()}: {v:.4f}")

    # Save Metrics to JSON (Required by Artifact Validation)
    with open(f'{REPORTS_METRICS_PATH}/test_metrics.json', 'w') as f:
        json.dump(metrics, f, indent=4)
    print(f"\nMetrics saved to {REPORTS_METRICS_PATH}/test_metrics.json")

    # --- Visualizations ---
    print("\nGenerating Visualizations...")
    plot_confusion_matrix(y_test, y_pred, f'{REPORTS_FIG_PATH}/model_eval_confusion_matrix.png')
    plot_roc_curve(y_test, y_prob, metrics['roc_auc'], f'{REPORTS_FIG_PATH}/model_eval_roc_curve.png')
    plot_precision_recall_curve(y_test, y_prob, f'{REPORTS_FIG_PATH}/model_eval_pr_curve.png')
    plot_prediction_distribution(y_prob, y_test, f'{REPORTS_FIG_PATH}/model_eval_pred_dist.png')
    plot_calibration_curve(y_test, y_prob, f'{REPORTS_FIG_PATH}/model_eval_calibration.png')

    print("\nEvaluation Phase Complete.")

if __name__ == "__main__":
    evaluate_model()