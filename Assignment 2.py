# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 14:26:05 2022

@author: Deeksha
"""
import numpy as np
import pandas as pd

def Agriculture(filename):
    df1=pd.read_csv(filename, skiprows=4)
    df1= df1.iloc[:6,5:10]
    df2= df1.T
    print(df1)
    print(df2)
    return df1,df2
Agriculture("API_AG.LND.AGRI.ZS_DS2_en_csv_v2_4669757.csv")