from extract import extract_data
from transform import transform_data
from load import load_data

def run_pipeline():
    """
    Run the full ETL pipeline: Extract -> Transform -> Load
    """
    print("🚀 STARTING FULL ETL PIPELINE...\n")
    
    # Extract
    df = extract_data()
    
    # Transform
    clean_df = transform_data(df)
    
    # Load
    engine = load_data(clean_df)
    
    print("\n🎉 PIPELINE COMPLETED SUCCESSFULLY!")
    print("You can now explore the data using SQLite or write SQL queries.")


if __name__ == "__main__":
    run_pipeline()