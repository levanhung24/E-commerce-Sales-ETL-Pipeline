import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DEFAULT_FILE_PATH = BASE_DIR / 'data' / 'messy_ecommerce_sales_data.csv'

def transform_data(df):
    print(" Starting transform...")
    
    df = df.copy()
    df.columns = df.columns.str.strip()   # Delete space
    
    #1. missing value
    
    print("Missing before processing: "), df.isnull().sum()
    
    # drop row missing Total
    df =df.dropna(subset=['Total'])
    
    #Fill missing Catefory by Unknown
    
    df['Category'] = df['Category'].fillna('Unknown')
    
    # Fill missing Quantity and Price by median (after convert to numerical)
    
    # 2. Change data type
    
    df['Order_Date'] = pd.to_datetime(df['Order_Date'], errors='coerce')
    df['Quantity'] = pd.to_numeric(df['Quantity'], errors = 'coerce')
    df['Price'] = pd.to_numeric(df['Price'],errors='coerce')
    
    #Fill missing Quanitty and Price after convert
    
    df['Quantity'] = df['Quantity'].fillna(df['Quantity'].median())
    df['Price'] = df["Price"].fillna(df['Price'].median())
    
    #3. Date processing
    
    invalid_dates = df['Order_Date'].isna().sum()
    print(f"Number of days that could not be converted: {invalid_dates}")
    df = df.dropna(subset=['Order_Date'])
    
    # Cast the datetime type again.
    df['Order_Date'] = pd.to_datetime(df['Order_Date'])
    
    #Create Year and Month
    df['Year'] = df['Order_Date'].dt.year
    df['Month'] = df['Order_Date'].dt.month
    
    # Profit Margin
    df['Profit_Margin'] = (df['Total']/(df['Quantity'] * df['Price']) * 100).round(2)
    
    #4. duplicate
    df = df.drop_duplicates()
    
    #5.Check after transform
    print("Missing sau transform:", df.isnull().sum())
    print(f"Shape sau transform: {df.shape}")
    print("\nSuccessful Transformation")
    
    return df
    
    #Test
if __name__ =="__main__":
    from extract import extract_data
    df = extract_data()
    clean_df = transform_data(df)
    print(clean_df.head())
    
    
# if __name__ == "__main__":
#     print("=== TEST PIPELINE ===")
#     try:
#         from extract import extract_data
        
#         df = extract_data()         
#         print("Extract complete, shape:", df.shape)
        
#         clean_df = transform_data(df)
#         print("Transform xong, shape:", clean_df.shape)
#         print(clean_df.head(3))
        
#     except Exception as e:
#         print("ERROS:", str(e))