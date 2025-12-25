import streamlit as st
import os
from PIL import Image

st.markdown("# 📊 Model Performance Dashboard")
st.markdown("### Technical Evaluation Metrics")

# --- METRICS ROW ---
col1, col2, col3 = st.columns(3)
col1.metric("ROC-AUC Score", "0.7812", delta="Pass (>0.75)")
col2.metric("Accuracy", "79.4%", delta="+2.1%")
col3.metric("Churn Rate (Test)", "32.0%", delta="Normal")

st.divider()

# --- VISUALIZATIONS ---
# We load the images we generated in src/04_eda.py and src/06_model_evaluation.py
# Paths are relative to where you run 'streamlit run app/main.py'
figures_dir = os.path.join("reports", "figures")

col_a, col_b = st.columns(2)

with col_a:
    st.markdown("#### 1. Confusion Matrix")
    st.caption("Shows True Positives vs False Positives")
    cm_path = os.path.join(figures_dir, "confusion_matrix.png")
    if os.path.exists(cm_path):
        st.image(Image.open(cm_path), width='stretch')
    else:
        st.warning("Confusion Matrix not found. Run src/06_model_evaluation.py")

with col_b:
    st.markdown("#### 2. Feature Importance")
    st.caption("Which factors drive customer churn?")
    fi_path = os.path.join(figures_dir, "feature_importance.png")
    if os.path.exists(fi_path):
        st.image(Image.open(fi_path), width='stretch')
    else:
        st.warning("Feature Importance not found. Run src/06_model_evaluation.py")

st.divider()

st.markdown("#### 3. Churn Distribution")
dist_path = os.path.join(figures_dir, "churn_distribution.png")
if os.path.exists(dist_path):
    st.image(Image.open(dist_path), width='stretch')
else:
    st.warning("Churn Distribution not found. Run src/04_eda.py")