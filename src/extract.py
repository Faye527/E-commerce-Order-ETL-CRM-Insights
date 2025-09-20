# src/extract.py

import pandas as pd
import glob
import os

RAW_PATH = "./data/raw_data/*.csv"
OUTPUT_PATH = "./data/processed_data/"  

os.makedirs(OUTPUT_PATH, exist_ok=True)

def load_and_combine_csv():
    all_files = glob.glob(RAW_PATH)
    df_list = []

    for file in all_files:
        df = pd.read_csv(file)
        df["source_file"] = os.path.basename(file)  
        df_list.append(df)

    combined = pd.concat(df_list, ignore_index=True)

    output_file = os.path.join(OUTPUT_PATH, "combined_orders.csv")
    combined.to_csv(output_file, index=False)

    return combined
if __name__ == "__main__":
    load_and_combine_csv()


