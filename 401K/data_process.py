import pyreadr
import pandas as pd

#Using pyreader to read the RData file into pd df

def load_rdata(filepath):
    readable = pyreadr.read_r(filepath)
    return readable