import os
import pandas as pd

def convert_xlsx_to_csv(xlsx_file, csv_file):
    try:
        # Read the Excel file
        df = pd.read_excel(xlsx_file)
        
        # Save to CSV
        df.to_csv(csv_file, index=False)
        print(f"Successfully converted {xlsx_file} to {csv_file}")

    except Exception as e:
        print(f"Error converting {xlsx_file} to {csv_file}: {e}")

if __name__ == "__main__":
    input_excel = r"C:\Users\koemhort.leng\Desktop\EWS_NPL_V2\dataset\Data 2026-07-31 V2.xlsx"  # Change this to your input directory
    output_csv = r"C:\Users\koemhort.leng\Desktop\EWS_NPL_V2\Data_2026-07-31.csv"  # Change this to your output directory
    convert_xlsx_to_csv(input_excel, output_csv)
