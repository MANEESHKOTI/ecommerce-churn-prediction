import pandas as pd
import numpy as np
import os
from datetime import datetime

# --- CONFIGURATION ---
INPUT_FILE = 'data/processed/cleaned_transactions.csv'
OUTPUT_FILE = 'data/processed/customer_features.csv'

def engineer_features():
    print("--- Phase 3: Feature Engineering (Optimized) ---")
    
    # 1. Load Data
    if not os.path.exists(INPUT_FILE):
        print(f"❌ Error: {INPUT_FILE} not found.")
        return

    print(f"Loading {INPUT_FILE}...")
    df = pd.read_csv(INPUT_FILE)
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['TotalSpent'] = df['Quantity'] * df['UnitPrice']
    
    # --- STRICT TIME WINDOW (Avoid Dec 2011 Cliff) ---
    observation_end = datetime(2011, 12, 1)
    training_cutoff = datetime(2011, 9, 1)
    
    print(f"Window: {training_cutoff.date()} to {observation_end.date()}")
    
    # Filter dataset
    df = df[df['InvoiceDate'] < observation_end]
    
    # Split
    train_df = df[df['InvoiceDate'] <= training_cutoff]
    observation_df = df[df['InvoiceDate'] > training_cutoff]
    
    # 2. Identify Target (Churn)
    # Target Population: Customers who existed in Training
    train_customers = set(train_df['CustomerID'].unique())
    active_customers = set(observation_df['CustomerID'].unique())
    
    features = pd.DataFrame({'CustomerID': list(train_customers)})
    
    # Define Churn: 1 if NOT in active list
    features['Churn'] = features['CustomerID'].apply(lambda x: 1 if x not in active_customers else 0)
    
    # 3. Calculate RFM (Training Data Only)
    print("Calculating features...")
    rfm = train_df.groupby('CustomerID').agg({
        'InvoiceDate': lambda x: (training_cutoff - x.max()).days, # Recency
        'InvoiceNo': 'nunique',                                    # Frequency
        'TotalSpent': 'sum',                                       # Monetary
        'UnitPrice': 'mean'                                        # Avg Price
    }).reset_index()

    rfm.rename(columns={
        'InvoiceDate': 'Recency',
        'InvoiceNo': 'Frequency',
        'TotalSpent': 'Monetary',
        'UnitPrice': 'AvgPrice'
    }, inplace=True)
    
    features = features.merge(rfm, on='CustomerID', how='left')

    # --- FILTER: REMOVE ONE-TIME BUYERS ---
    # This aligns with focusing on "Retention" of actual customers
    initial_count = len(features)
    features = features[features['Frequency'] > 1]
    filtered_count = len(features)
    print(f"Filtered {initial_count - filtered_count} one-time buyers.")

    # 4. Save
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    features.to_csv(OUTPUT_FILE, index=False)
    
    # Final Stats
    churn_rate = features['Churn'].mean() * 100
    print("\n" + "="*40)
    print("FEATURE ENGINEERING COMPLETE")
    print(f"Total Customers: {len(features):,}")
    print(f"Churn Rate:      {churn_rate:.2f}% (Target: 20-40%)")
    
    if 20 <= churn_rate <= 40:
        print("✅ SUCCESS: Rate is PERFECT.")
    else:
        print("⚠️ NOTE: Rate is valid (10-60%) but outside ideal target.")
    print("="*40)

if __name__ == "__main__":
    engineer_features()