import pandas as pd
import numpy as np
import os
import joblib
import json
import sys

# --- CONFIGURATION ---
# Robust path determination relative to this script
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Paths to artifacts generated in Step 05
MODEL_PATH = os.path.join(BASE_DIR, 'models', 'best_model.pkl')
SCALER_PATH = os.path.join(BASE_DIR, 'models', 'preprocessor.pkl') 
FEATURE_NAMES_PATH = os.path.join(BASE_DIR, 'data', 'processed', 'feature_names.json')
# ---------------------

class ModelService:
    def __init__(self):
        self.model = None
        self.scaler = None
        self.feature_names = None
        self.load_artifacts()

    def load_artifacts(self):
        """Loads Model, Scaler, and the exact Feature Names used in training."""
        try:
            print("Loading artifacts...")
            # Check existence
            if not os.path.exists(MODEL_PATH):
                raise FileNotFoundError(f"Model not found at {MODEL_PATH}")
            if not os.path.exists(SCALER_PATH):
                raise FileNotFoundError(f"Scaler not found at {SCALER_PATH}")
            if not os.path.exists(FEATURE_NAMES_PATH):
                raise FileNotFoundError(f"Feature names not found at {FEATURE_NAMES_PATH}")

            # Load
            self.model = joblib.load(MODEL_PATH)
            self.scaler = joblib.load(SCALER_PATH)
            
            # Load JSON feature names
            with open(FEATURE_NAMES_PATH, 'r') as f:
                self.feature_names = json.load(f)

            print(f"✅ Model loaded successfully.")
            print(f"   Expecting {len(self.feature_names)} features.")
            
        except Exception as e:
            print(f"❌ CRITICAL ERROR: Artifacts missing or invalid.")
            print(f"   Error details: {e}")
            print("   PLEASE RUN 'python src/05_model_training.py' FIRST.")

    def preprocess_input(self, data):
        """
        Aligns input data exactly to the training features to prevent mismatch errors.
        """
        if self.feature_names is None:
            print("❌ Error: Feature names not loaded. Cannot process input.")
            return None

        # 1. Convert input to DataFrame
        if isinstance(data, dict):
            df = pd.DataFrame([data])
        else:
            df = data.copy()

        # 2. FILL MISSING COLUMNS
        # If the user input is missing columns (e.g., encoded categories), fill with 0
        for col in self.feature_names:
            if col not in df.columns:
                df[col] = 0.0

        # 3. REORDER COLUMNS (Critical for XGBoost/Neural Net)
        # Drop any extra columns not in training, and ensure exact order
        try:
            df_final = df[self.feature_names]
        except KeyError as e:
            print(f"❌ Error aligning columns: {e}")
            return None
        
        return df_final

    def predict(self, input_data):
        """
        Performs a single prediction.
        Returns: (Class (0/1), Probability (0.0-1.0))
        """
        if not self.model:
            return None, None

        try:
            # Align features
            processed_df = self.preprocess_input(input_data)
            
            if processed_df is None:
                return None, None

            # Scale
            scaled_data = self.scaler.transform(processed_df)
            
            # Predict
            prediction = self.model.predict(scaled_data)[0]
            
            # Handle probabilities
            if hasattr(self.model, "predict_proba"):
                probability = self.model.predict_proba(scaled_data)[0][1]
            else:
                probability = float(prediction)
            
            return int(prediction), float(probability)
        except Exception as e:
            print(f"❌ Prediction Error: {e}")
            return None, None

    def predict_batch(self, df):
        """
        Performs batch predictions on a DataFrame.
        Returns: (Predictions Array, Probabilities Array)
        """
        if not self.model:
            return None, None

        try:
            # Align features
            processed_df = self.preprocess_input(df)
            
            if processed_df is None:
                return None, None

            # Scale
            scaled_data = self.scaler.transform(processed_df)
            
            # Predict
            preds = self.model.predict(scaled_data)
            
            if hasattr(self.model, "predict_proba"):
                probs = self.model.predict_proba(scaled_data)[:, 1]
            else:
                probs = preds.astype(float)
            
            return preds, probs
        except Exception as e:
            print(f"❌ Batch Prediction Error: {e}")
            return None, None

# Create a singleton instance to be imported by the App
model_service = ModelService()

# Helper functions for cleaner imports in Streamlit
def predict(input_data):
    return model_service.predict(input_data)

def predict_proba(input_data):
    return model_service.predict(input_data)[1]

if __name__ == "__main__":
    # Internal Test to verify the fix works
    print("\n--- Testing Inference API ---")
    
    # Dummy data missing some columns (to test auto-fill)
    test_data = {
        'Recency': 20, 
        'Frequency': 2, 
        'TotalSpent': 100,
        # Missing 'AvgOrderValue' and categorical columns
    }
    
    pred, prob = model_service.predict(test_data)
    
    if pred is not None:
        print(f"✅ Test Successful!")
        print(f"   Prediction: {pred}")
        print(f"   Probability: {prob:.4f}")
    else:
        print("❌ Test Failed.")