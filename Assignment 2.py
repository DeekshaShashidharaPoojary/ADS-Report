# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 14:26:05 2022

@author: Deeksha
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def Agriculture(filename):
    df1=pd.read_csv(filename, skiprows=4)
    df1 = df1.drop(['Country Code','Indicator Name','Indicator Code'], axis=1)
    df1= df1.iloc[90:96,[0,41,42,43,44,45]]
    df1=df1.dropna(axis=1)
    df2= df1.T
    print(df1)
    print(df2)
    return df1,df2

a,b=Agriculture("API_AG.LND.AGRI.ZS_DS2_en_csv_v2_4669757.csv")

plt.figure(dpi=144)
plt.plot(a["Country Name"],a["2000"], label="2000")
plt.plot(a["Country Name"],a["2001"], label="2001")
plt.plot(a["Country Name"],a["2002"], label="2002")
plt.plot(a["Country Name"],a["2003"], label="2003")
plt.plot(a["Country Name"],a["2004"], label="2004")
plt.xlabel("Country Name")
plt.ylabel("Year")
plt.legend() 
plt.show()
