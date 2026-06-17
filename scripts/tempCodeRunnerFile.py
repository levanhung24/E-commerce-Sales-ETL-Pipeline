(subset=['Order_Date'])
    
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