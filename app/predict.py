import streamlit as st
import sys
import os

# --- PATH FIX ---
# Calculate path to root (same logic as your other files)
current_file_path = os.path.abspath(__file__)
project_root = os.path.dirname(os.path.dirname(current_file_path))
if project_root not in sys.path:
    sys.path.append(project_root)

# Import Model Service
try:
    from src._inference_api import model_service
except ImportError:
    # Handle case where main.py might have already set the path
    pass 

def run():
    st.markdown("# 🔮 Quick Predict")
    st.markdown("Run a prediction directly from the main app interface.")

    # --- INPUT FORM ---
    with st.form("root_prediction_form"):
        col1, col2 = st.columns(2)
        with col1:
            recency = st.number_input("Recency", 0, 365, 10)
            frequency = st.number_input("Frequency", 1, 1000, 5)
        with col2:
            monetary = st.number_input("Total Spend (£)", 0.0, 100000.0, 500.0)
            avg_price = st.number_input("Avg Unit Price (£)", 0.0, 1000.0, 25.0)

        if st.form_submit_button("Predict"):
            input_data = {
                'Recency': recency, 'Frequency': frequency,
                'TotalSpent': monetary, 'AvgOrderValue': avg_price
            }
            # Predict
            try:
                pred, prob = model_service.predict(input_data)
                if pred == 1:
                    st.error(f"🚨 **High Churn Risk** ({prob:.1%})")
                else:
                    st.success(f"✅ **Loyal Customer** ({prob:.1%})")
            except Exception as e:
                st.error(f"Prediction Error: {e}")