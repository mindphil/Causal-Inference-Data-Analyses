import pyreadr
import pandas as pd

#Read the R data file into pd df

def transform(filepath):
    # Read the R data file - returns OrderedDict
    r_data = pyreadr.read_r(filepath)
    print("Available datasets in R file:")
    for key in r_data.keys():
        print(f"  - {key}: shape {r_data[key].shape}")
        first_key = list(r_data.keys())[0]
    return r_data[first_key]

# Option 2: If you know the specific dataset name, use it directly
    # return r_data['sipp1991']  # Replace with actual dataset name