import streamlit as st
import os
from PIL import Image

st.markdown("# 📊 Model Performance Dashboard")
st.markdown("### Technical Evaluation Metrics")

# --- METRICS ROW ---
# (Keeping your original metrics exactly as they were)
col1, col2, col3 = st.columns(3)
col1.metric("ROC-AUC Score", "0.7812", delta="Pass (>0.75)")
col2.metric("Accuracy", "79.4%", delta="+2.1%")
col3.metric("Churn Rate (Test)", "32.0%", delta="Normal")

st.divider()

# --- MAIN VISUALIZATIONS ---
figures_dir = os.path.join("reports", "figures")

# Define the critical images we ALWAYS want to show at the top
priority_images = {
    "confusion_matrix.png": "#### 1. Confusion Matrix",
    "feature_importance.png": "#### 2. Feature Importance",
    "churn_distribution.png": "#### 3. Churn Distribution"
}

# 1. Row 1: Confusion Matrix & Feature Importance
col_a, col_b = st.columns(2)

with col_a:
    st.markdown(priority_images["confusion_matrix.png"])
    st.caption("Shows True Positives vs False Positives")
    cm_path = os.path.join(figures_dir, "confusion_matrix.png")
    if os.path.exists(cm_path):
        st.image(Image.open(cm_path), use_container_width=True)
    else:
        st.warning("Confusion Matrix not found.")

with col_b:
    st.markdown(priority_images["feature_importance.png"])
    st.caption("Which factors drive customer churn?")
    fi_path = os.path.join(figures_dir, "feature_importance.png")
    if os.path.exists(fi_path):
        st.image(Image.open(fi_path), use_container_width=True)
    else:
        st.warning("Feature Importance not found.")

st.divider()

# 2. Row 2: Churn Distribution (Full Width)
st.markdown(priority_images["churn_distribution.png"])
dist_path = os.path.join(figures_dir, "churn_distribution.png")
if os.path.exists(dist_path):
    st.image(Image.open(dist_path), use_container_width=True)
else:
    st.warning("Churn Distribution not found.")

# --- NEW SECTION: EDA GALLERY ---
st.divider()
st.markdown("### 🖼️ Exploratory Analysis (EDA) Deep Dive")
st.markdown("Additional insights from the data analysis pipeline.")

# 3. Dynamic Gallery for the rest of the images
if os.path.exists(figures_dir):
    # Get all files in the directory
    all_files = os.listdir(figures_dir)
    
    # Filter for PNGs that we haven't shown yet
    gallery_files = [f for f in all_files if f.endswith(".png") and f not in priority_images]
    
    if gallery_files:
        # Display in a grid of 2 columns
        cols = st.columns(2)
        for i, img_file in enumerate(gallery_files):
            img_path = os.path.join(figures_dir, img_file)
            
            # Clean up filename for the title (e.g., "monthly_sales.png" -> "Monthly Sales")
            img_title = img_file.replace(".png", "").replace("_", " ").title()
            
            with cols[i % 2]:  # Toggle between col 0 and col 1
                st.markdown(f"**{img_title}**")
                st.image(Image.open(img_path), use_container_width=True)
    else:
        st.info("No additional EDA images found in reports/figures.")
else:
    st.error(f"Directory not found: {figures_dir}")