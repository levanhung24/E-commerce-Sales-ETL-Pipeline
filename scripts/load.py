from sqlalchemy import create_engine
import os

def load_data(df, table_name="sales", db_name="ecommerce.db"):
    """
    Load transformed data into SQLite database.
    """
    # Create data folder if not exists
    os.makedirs("data", exist_ok=True)
    
    engine = create_engine(f'sqlite:///data/{db_name}')
    
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    
    print(f"✅ Successfully loaded {len(df)} rows into table '{table_name}' in {db_name}")
    return engine