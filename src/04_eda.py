import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# --- CONFIGURATION ---
INPUT_FILE = 'data/processed/customer_features.csv'
FIGURES_DIR = 'reports/figures'
# ---------------------

def perform_eda():
    print("--- Phase 5: Exploratory Data Analysis (Automated) ---")
    
    # 1. Load Data
    if not os.path.exists(INPUT_FILE):
        print(f"❌ Error: {INPUT_FILE} not found. Run Phase 3 first.")
        return

    df = pd.read_csv(INPUT_FILE)
    os.makedirs(FIGURES_DIR, exist_ok=True)
    
    # Set plot style
    sns.set(style="whitegrid")

    # --- CHART 1: CHURN DISTRIBUTION (Target Balance) ---
    print("Generating Churn Distribution Chart...")
    plt.figure(figsize=(6, 4))
    ax = sns.countplot(x='Churn', data=df, palette='viridis')
    plt.title('Churn Class Distribution')
    plt.xlabel('Churn (0=Retained, 1=Churned)')
    plt.ylabel('Count')
    
    # Add labels
    for p in ax.patches:
        ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='baseline')
    
    plt.savefig(f'{FIGURES_DIR}/churn_distribution.png')
    plt.close()
    print(f"✅ Saved: {FIGURES_DIR}/churn_distribution.png")

    # --- CHART 2: CORRELATION MATRIX (Feature Relationships) ---
    print("Generating Correlation Matrix...")
    plt.figure(figsize=(12, 10))
    # Select only numeric columns for correlation
    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    corr = numeric_df.corr()
    
    sns.heatmap(corr, annot=False, cmap='coolwarm', linewidths=0.5)
    plt.title('Feature Correlation Matrix')
    plt.tight_layout()
    
    plt.savefig(f'{FIGURES_DIR}/correlation_matrix.png')
    plt.close()
    print(f"✅ Saved: {FIGURES_DIR}/correlation_matrix.png")

    # --- CHART 3: RECENCY vs. CHURN (Behavioral Check) ---
    print("Generating Recency Boxplot...")
    plt.figure(figsize=(8, 6))
    sns.boxplot(x='Churn', y='Recency', data=df, palette='Set2')
    plt.title('Recency Distribution by Churn Status')
    plt.savefig(f'{FIGURES_DIR}/recency_boxplot.png')
    plt.close()
    print(f"✅ Saved: {FIGURES_DIR}/recency_boxplot.png")
    
    print("\n--- EDA Complete. Check 'reports/figures/' folder. ---")

if __name__ == "__main__":
    perform_eda()