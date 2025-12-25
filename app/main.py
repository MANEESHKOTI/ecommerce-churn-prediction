import streamlit as st
import os
import sys

# Add project root to path so we can import src
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Page Config (Must be the first command)
st.set_page_config(
    page_title="Churn Prediction System",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Main Landing Content ---
def main():
    st.title("🛍️ E-Commerce Churn Prediction AI")
    
    st.markdown("""
    ### Welcome to the Enterprise Churn Prediction System
    
    This application allows you to predict customer churn risk using a trained **XGBoost Classifier**.
    
    #### 📂 Application Modules (Select from Sidebar):
    
    * **🏠 Home:** Project Overview and Key Metrics.
    * **👤 Single Prediction:** Predict churn for one customer interactively.
    * **📂 Batch Prediction:** Upload a CSV to score thousands of customers.
    * **📊 Dashboard:** View model performance (ROC-AUC, Confusion Matrix).
    * **📄 Documentation:** Technical details and definitions.
    
    ---
    **Status:** ✅ Model Loaded | ✅ Pipeline Active
    """)
    
    st.sidebar.success("Select a page above.")

if __name__ == "__main__":
    main()