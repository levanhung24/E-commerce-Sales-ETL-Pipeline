# E-commerce Sales ETL Pipeline

## Project Overview
This project demonstrates a complete **ETL (Extract, Transform, Load)** pipeline for processing messy real-world e-commerce sales data. 

The pipeline handles data cleaning, type conversion, feature engineering, and loads the cleaned data into a PostgreSQL database.

## Tech Stack
- **Language**: Python 3
- **Data Processing**: Pandas
- **Database**: PostgreSQL
- **ETL Architecture**: Modular scripts (extract, transform, load)

## Features
- Clean messy data (handling missing values, incorrect data types, duplicates, leading spaces in column names)
- Data type conversion (datetime, numeric)
- Feature Engineering (`Year`, `Month`, `Profit_Margin`)
- Modular code structure for easy maintenance
- Load data into PostgreSQL database


## How to Run

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the full ETL pipeline
python scripts/main_pipeline.py
