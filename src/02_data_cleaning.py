import pandas as pd
import numpy as np
import os
import json
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)

# Construct path relative to project root
RAW_DATA_PATH = os.path.join(project_root, "data", "raw", "online_retail_II.xlsx")
# --- CONFIGURATION ---
PROCESSED_DIR = 'data/processed'
OUTPUT_FILE = os.path.join(PROCESSED_DIR, 'cleaned_transactions.csv')
STATS_FILE = os.path.join(PROCESSED_DIR, 'cleaning_statistics.json')

class DataCleaner:
    def __init__(self):
        self.df = None
        self.stats = {}

    def load_data(self):
        print(f"Loading raw data from {RAW_DATA_PATH}...")
        try:
            # Load both sheets as we did in Phase 1
            all_sheets = pd.read_excel(RAW_DATA_PATH, sheet_name=None)
            self.df = pd.concat(all_sheets.values(), ignore_index=True)
            self.stats['original_rows'] = len(self.df)
            print(f"Initial Row Count: {len(self.df):,}")
        except Exception as e:
            print(f"❌ Error loading data: {e}")
            sys.exit(1)

    def clean(self):
        print("--- Starting Cleaning Pipeline ---")
        
        # 1. Standardize Column Names
        print("Step 1: Standardizing columns...")
        self.df.rename(columns={
            'Customer ID': 'CustomerID',
            'User ID': 'CustomerID',
            'Price': 'UnitPrice',
            'Invoice': 'InvoiceNo',
            'Data': 'InvoiceDate'
        }, inplace=True)

        # 2. Remove Missing CustomerIDs
        print("Step 2: Removing missing CustomerIDs...")
        before = len(self.df)
        self.df = self.df.dropna(subset=['CustomerID'])
        self.stats['missing_id_removed'] = before - len(self.df)

        # 3. Remove Cancellations (Invoice starts with 'C')
        print("Step 3: Removing cancellations...")
        self.df['InvoiceNo'] = self.df['InvoiceNo'].astype(str)
        self.df = self.df[~self.df['InvoiceNo'].str.startswith('C')]
        
        # 4. Remove Negative/Zero Quantities & Prices
        print("Step 4: Removing invalid values...")
        self.df = self.df[(self.df['Quantity'] > 0) & (self.df['UnitPrice'] > 0)]
        
        # 5. Handle Duplicates
        print("Step 5: Removing duplicates...")
        self.df = self.df.drop_duplicates()

        # Final Stats
        self.stats['final_rows'] = len(self.df)
        self.stats['retention_rate'] = (self.stats['final_rows'] / self.stats['original_rows']) * 100

    def save_data(self):
        os.makedirs(PROCESSED_DIR, exist_ok=True)
        
        print(f"Saving cleaned data to {OUTPUT_FILE}...")
        self.df.to_csv(OUTPUT_FILE, index=False)
        
        # Save statistics JSON (Required by PDF)
        with open(STATS_FILE, 'w') as f:
            json.dump(self.stats, f, indent=4)
            
        print("\n" + "="*40)
        print(f"CLEANING COMPLETE")
        print(f"Original Rows: {self.stats['original_rows']:,}")
        print(f"Cleaned Rows:  {self.stats['final_rows']:,}")
        print(f"Retention Rate: {self.stats['retention_rate']:.2f}%")
        print("="*40)

if __name__ == "__main__":
    cleaner = DataCleaner()
    cleaner.load_data()
    cleaner.clean()
    cleaner.save_data()