import pyreadr
import pandas as pd

#Using pyreader to read the rdata, and create df

def load_rdata(filepath):
    readable = pyreadr.read_r(filepath)
    return readable

#There are over 9000 observations in the dataset,
# for data loading and initial exploration, what is really important?
    # 401k offering, 401k participation and net financial assets.
    # Maybe I extract the means of these variables, and use that for the df in the notebook to better represent the statistics?

def whats_important(): #parameter should be df or filepath?
    #loop to iterate over all rows, find e401, p401, net_tfa, scrap the rest
    #work in 'describe' to get sample means, ect.
     


# & then descriptive statistics and visualizations
# I need to determine what is really important.