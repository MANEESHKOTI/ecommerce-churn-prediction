import pandas as pd
import os
import sys

# Define the exact path you confirmed
RAW_DATA_PATH = '/Users/maneeshkoti/Documents/ecommerce-churn-prediction/data/raw/online_retail_II.xlsx'
PROFILE_OUTPUT_PATH = 'data/raw/data_profile.txt'

def acquire_data():
    print("--- Phase 1: Data Acquisition ---")
    
    # 1. Verify File Exists
    if not os.path.exists(RAW_DATA_PATH):
        print(f"❌ CRITICAL ERROR: File not found at {RAW_DATA_PATH}")
        sys.exit(1)
        
    print(f"Found file at: {RAW_DATA_PATH}")
    print("Reading Excel sheets... (This takes a minute, please wait)")

    try:
        # 2. Load BOTH sheets (Year 2009-2010 and Year 2010-2011)
        # sheet_name=None reads all sheets into a dictionary
        all_sheets = pd.read_excel(RAW_DATA_PATH, sheet_name=None)
        
        # 3. Combine them into one dataframe
        df = pd.concat(all_sheets.values(), ignore_index=True)
        print(f"✅ Data Loaded Successfully.")
        print(f"   Total Rows: {len(df):,}")
        print(f"   Total Columns: {len(df.columns)}")
        
        # 4. Generate the Data Profile (Required by your file structure)
        generate_profile(df)
        
    except Exception as e:
        print(f"❌ Error reading Excel file: {e}")
        sys.exit(1)

def generate_profile(df):
    """Generates the data_profile.txt artifact."""
    print("Generating data profile...")
    
    with open(PROFILE_OUTPUT_PATH, 'w') as f:
        f.write("DATASET PROFILE\n")
        f.write("================\n\n")
        f.write(f"Source: {RAW_DATA_PATH}\n")
        f.write(f"Total Rows: {len(df)}\n")
        f.write(f"Total Columns: {len(df.columns)}\n")
        f.write(f"Column Names: {list(df.columns)}\n\n")
        f.write("Missing Values:\n")
        f.write(df.isnull().sum().to_string())
        f.write("\n\nSample Data:\n")
        f.write(df.head(3).to_string())
        
    print(f"✅ Profile saved to {PROFILE_OUTPUT_PATH}")
    print("--- Phase 1 Complete ---")

if __name__ == "__main__":
    acquire_data()