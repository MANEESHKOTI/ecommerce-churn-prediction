import streamlit as st
import os
import sys

# --- NEW IMPORT ---
import predict  # Import the file you just created

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

st.set_page_config(
    page_title="Churn Prediction System",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    # --- MODIFICATION START ---
    # Add a toggle in the sidebar to switch views within main.py
    app_mode = st.sidebar.radio("🔎 Main Menu", ["Project Overview", "Quick Predict"])

    if app_mode == "Quick Predict":
        # Run the code from your new file
        predict.run()
    
    else:
        # Keep your existing "GOLD" content here
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
    # --- MODIFICATION END ---

if __name__ == "__main__":
    main()