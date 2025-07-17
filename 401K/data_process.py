import pyreadr
import pandas as pd

#Using pyreader to read the rdata, and create df

def load_rdata(filepath):
    readable = pyreadr.read_r(filepath)
    return readable