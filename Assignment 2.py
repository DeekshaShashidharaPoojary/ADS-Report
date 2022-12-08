# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 14:26:05 2022

@author: Deeksha
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def Agriculture(filename):
    df1= pd.read_csv(filename, skiprows=4) 
    df1= df1.drop(['Country Code','Indicator Name','Indicator Code'], axis=1)
    df1= df1.iloc[200:206,[0,41,42,43,44,45]]
    df1= df1.dropna(axis=1)
    df2= df1.set_index('Country Name').T
    return df1,df2

a, b=Agriculture("API_SP.POP.GROW_DS2_en_csv_v2_4701208.csv")
print(a)
print(b)
b.plot()
plt.legend(loc='best')


c, d=Agriculture("API_EG.FEC.RNEW.ZS_DS2_en_csv_v2_4697469.csv")
print(c)
print(d)

d.plot(kind='line', rot=0)
plt.legend(loc='best')

def resource(filename1):
    df= pd.read_csv(filename1, skiprows=4)
    print(df)
    return df
resource("API_EG.USE.ELEC.KH.PC_DS2_en_csv_v2_4697520.csv")

