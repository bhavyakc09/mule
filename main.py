import pandas as pd
import os

input_files = os.environ['INPUT_FILE'].split(',')
output_file = os.environ['OUTPUT_FILE']

dfs = []
for file in input_files:
    df = pd.read_csv(file)
    dfs.append(df)

merged = pd.concat(dfs, axis=1)
merged.to_excel(output_file, index=False)
