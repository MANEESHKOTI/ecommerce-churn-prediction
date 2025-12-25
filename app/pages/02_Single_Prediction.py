import streamlit as st
import sys
import os

# --- PATH FIX: FORCE PYTHON TO FIND THE 'src' FOLDER ---
# Get the absolute path of the current file (app/pages/02_Single_Prediction.py)
current_file_path = os.path.abspath(__file__)
# Go up 3 levels: 02_Single... -> pages -> app -> ecommerce-churn-prediction (ROOT)
project_root = os.path.dirname(os.path.dirname(os.path.dirname(current_file_path)))
# Add the root to Python's search path
if project_root not in sys.path:
    sys.path.append(project_root)
# -------------------------------------------------------

# NOW import the src module
try:
    from src._inference_api import model_service
except ImportError as e:
    st.error(f"❌ Critical Import Error: {e}")
    st.stop()

st.markdown("# 👤 Single Customer Prediction")
st.markdown("Enter customer metrics below to predict churn probability.")

# --- INPUT FORM ---
with st.form("prediction_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        recency = st.number_input(
            "Recency (Days since last purchase)", 
            min_value=0, max_value=365, value=10,
            help="How many days ago was their last order?"
        )
        frequency = st.number_input(
            "Frequency (Total orders)", 
            min_value=1, max_value=1000, value=5,
            help="Total number of invoices for this customer."
        )
        
    with col2:
        monetary = st.number_input(
            "Monetary (Total Spend £)", 
            min_value=0.0, max_value=100000.0, value=500.0,
            help="Total lifetime spend."
        )
        avg_price = st.number_input(
            "Average Unit Price (£)",
            min_value=0.0, max_value=1000.0, value=25.0,
            help="Average price of items they buy."
        )

    # Submit Button
    submitted = st.form_submit_button("Predict Churn Risk")

# --- LOGIC ---
if submitted:
    input_data = {
        'Recency': recency,
        'Frequency': frequency,
        'TotalSpent': monetary,
        'AvgOrderValue': avg_price
    }
    
    pred, prob = model_service.predict(input_data)
    
    if pred is not None:
        st.divider()
        st.markdown("### 🔍 Prediction Result")
        
        if pred == 1:
            st.error(f"🚨 **High Churn Risk** (Probability: {prob:.1%})")
            st.info("💡 **Recommendation:** Send immediate retention offer.")
        else:
            st.success(f"✅ **Loyal Customer** (Probability: {prob:.1%})")
            st.info("💡 **Recommendation:** Add to 'Loyalty Program' tier.")
    else:
        st.error("Error: Could not get prediction. Check terminal logs.")