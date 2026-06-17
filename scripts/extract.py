import pandas as pd
import os
from pathlib import Path

def extract_data(file_path = "data/messy_ecommerce_sales_data.csv"):
    if not os.path.exists(file_path):
        raise FileNotFoundError(F"File not found")
    
    df = pd.read_csv(file_path)
    print(f"Extraction succesful: {df.shape[0]} row, {df.shape[1]} columns")
    print("\n Columns: ", df.columns.tolist())
    return df

if __name__ == "__main__":
    df = extract_data()
    print(df.head())
