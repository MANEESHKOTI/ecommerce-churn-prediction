import streamlit as st
import pandas as pd
import sys
import os

# --- PATH FIX: FORCE PYTHON TO FIND THE 'src' FOLDER ---
current_file_path = os.path.abspath(__file__)
project_root = os.path.dirname(os.path.dirname(os.path.dirname(current_file_path)))
if project_root not in sys.path:
    sys.path.append(project_root)
# -------------------------------------------------------

try:
    from src._inference_api import model_service
except ImportError as e:
    st.error(f"❌ Critical Import Error: {e}")
    st.stop()

st.markdown("# 📂 Batch Prediction")
st.markdown("Upload a CSV file containing customer data to generate predictions for the entire list.")

# --- FILE UPLOADER ---
uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

# --- TEMPLATE ---
st.markdown("---")
st.markdown("#### Need a template?")
sample_data = {
    'Recency': [10, 200, 5],
    'Frequency': [5, 1, 20],
    'TotalSpent': [500, 50, 2000],
    'AvgOrderValue': [20, 10, 50]
}
sample_df = pd.DataFrame(sample_data)
csv = sample_df.to_csv(index=False).encode('utf-8')

st.download_button(
    "📥 Download Example CSV",
    csv,
    "example_input.csv",
    "text/csv",
    key='download-template'
)

# --- LOGIC ---
if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        st.write(f"✅ Uploaded {len(df)} rows.")
        
        if st.button("Run Batch Prediction"):
            with st.spinner("Analyzing customers..."):
                preds, probs = model_service.predict_batch(df)
                
                if preds is not None:
                    df['Churn_Prediction'] = preds
                    df['Churn_Probability'] = probs
                    
                    st.dataframe(df.head())
                    
                    result_csv = df.to_csv(index=False).encode('utf-8')
                    
                    st.success("Analysis Complete!")
                    st.download_button(
                        "📥 Download Results CSV",
                        result_csv,
                        "churn_predictions.csv",
                        "text/csv",
                        key='download-csv'
                    )
                else:
                    st.error("Error during prediction. Check terminal logs.")
                    
    except Exception as e:
        st.error(f"Error reading file: {e}")