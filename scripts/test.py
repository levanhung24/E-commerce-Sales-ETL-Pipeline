import pandas as pd
import os

print("=== DEBUG BẮT ĐẦU ===")
print("Thư mục hiện tại:", os.getcwd())

# Kiểm tra file có tồn tại không
file_path = "data/messy_ecommerce_sales_data.csv"
print(f"File tồn tại? {os.path.exists(file_path)}")

if os.path.exists(file_path):
    df = pd.read_csv(file_path)
    print("Đọc file thành công! Shape:", df.shape)
    print(df.columns.tolist())
    print(df.head(2))
else:
    print("❌ KHÔNG TÌM THẤY FILE!")