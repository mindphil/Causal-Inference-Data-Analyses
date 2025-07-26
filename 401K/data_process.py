import pyreadr
import pandas as pd

#Read the R data file into pd df

def read(filepath):
    r_data = pyreadr.read_r(filepath)
    df = list(r_data.values())[0]
    return df