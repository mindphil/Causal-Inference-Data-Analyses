import pyreadr
import pandas as pd

#Using pyreader to read the RData file into pd df

def transform(filepath):
    transformed = pyreadr.read_r(filepath)
    return transformed