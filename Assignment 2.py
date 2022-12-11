# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 14:26:05 2022

@author: Deeksha
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



#defining a fuction 
def Agriculture(filename):
    #reading the csv file 
    df1= pd.read_csv(filename, skiprows=4) 
    #dropping the columns
    df1= df1.drop(['Country Code','Indicator Name','Indicator Code'], axis=1)
    #selecting the specific rows and columns
    df1= df1.iloc[200:206,[0,41,42,43,44,45]]
    #dropping nan values
    df1= df1.dropna(axis=1)
    #setting the index and transposing dataframe
    df2= df1.set_index('Country Name').T
    #to return the dataframes
    return df1,df2

#assigning the variable to funtion called
a, b=Agriculture("API_SP.POP.GROW_DS2_en_csv_v2_4701208.csv")
print(a) #to get the the result of a
print(b) #to get the the result of b
plt.figure(dpi=144)#to create a figure and dpi is for clarity of the bar plot
b.plot() #plotting the line graph 
#will show the index value on the graph and set location to be shown
plt.legend(loc='upper right')
#assigning the title for the graph
plt.title("Population Growth")
plt.savefig('plot1.png')#saving the image


#assigning the variable to funtion called
c, d=Agriculture("API_EG.FEC.RNEW.ZS_DS2_en_csv_v2_4697469.csv")
print(c)#to get the the result of c
print(d)#to get the the result of d
plt.figure(dpi=144)#to create a figure and dpi is for clarity of the bar plot
d.plot()#plotting the line graph
#will show the index value on the graph and set location to be shown
plt.legend(loc='upper right')
#assigning the title for the graph
plt.title("Renewable Energy Consumption")
plt.savefig('plot2.png')#saving the image

#defining a fuction
def resource(filename1):
    #reading the csv file 
    df= pd.read_csv(filename1, skiprows=4)
    #dropping the columns
    df= df.drop(['Country Code','Indicator Name','Indicator Code'], axis=1)
    #selecting the specific rows and columns
    df= df.iloc[113:118,[0,31,32,33,34,35]]
    #dropping nan values
    df= df.dropna(axis=1)
    #setting the index and transposing dataframe
    df3= df.set_index('Country Name').T
    #to return the dataframes
    return df, df3
#assigning the variable to funtion called
x, y=resource("API_EG.USE.ELEC.KH.PC_DS2_en_csv_v2_4697520.csv")
print(x)#to get the the result of x
print(y)#to get the the result of y
plt.figure(dpi=144)#to create a figure and dpi is for clarity of the bar plot
#plotting the bar graph
y.plot(kind='bar', rot=0)
#assigning the title for the graph
plt.title("Energy Use")
plt.savefig('plot3.png')#saving the image

#assigning the variable to funtion called
p, q=resource("API_EG.USE.PCAP.KG.OE_DS2_en_csv_v2_4697327.csv")
print(p)#to get the the result of p
print(q)#to get the the result of q
plt.figure(dpi=144)#to create a figure and dpi is for clarity of the bar plot
#plotting the bar graph
q.plot(kind='bar', rot=0)
#assigning the title for the graph
plt.title("Electric Power consumptions")
plt.savefig('plot4.png')#saving the image

#defining a fuction
def climate_change(filename3):
    #reading the csv file
    df2=pd.read_csv(filename3, skiprows=4)
    #dropping the columns
    df2= df2.drop(['Country Code','Indicator Code'], axis=1)
    #selecting the particular country to plot for heatmap
    df2=df2.loc[df2["Country Name"]=='Qatar']
    #slecting the indicators to be plotted
    ind=["Urban population","Cereal yield (kg per hectare)","CO2 emissions (kt)",
         "Electricity production from oil sources (% of total)",
         "Arable land (% of land area)","Agricultural irrigated land (% of total agricultural land)",
         "Total greenhouse gas emissions (% change from 1990)",
         "Agriculture, forestry, and fishing, value added (% of GDP)",]
    #adding filter for indicator name based on indicator
    filter= df2["Indicator Name"].isin(ind)
    #selecting particular variable and assigning to a new dataframe
    df4=df2.loc[filter]
    #selecting the indicator name and the years
    df5=df4[['Indicator Name','1960','1980','2000','2010','2018','2019']]
    #transposing the dataframe 
    df5=df5.set_index("Indicator Name").T
    #replacing the nan values with 0
    df5= df5.fillna(0)
    #to return the dataframes
    return df2,df5

#assigning the variable to funtion called
s,h=climate_change("Master.csv")
print(s)#to get the the result of s
print(h)#to get the the result of h

#Function generates a correlation heatmap and size to plot vertical and horizontal 
def map_corr(df, size=10):
    #finding correlation of each columns
    corr = df.corr()
    #clarity for the subplots
    fig, ax = plt.subplots(figsize=(size, size))
    ax.matshow(corr, cmap='coolwarm')
    #plotting and setting ticks to column names
    plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
    plt.yticks(range(len(corr.columns)), corr.columns)
    

corr = h.corr()
print(corr)
#calling the funtion
map_corr(h)
#alot colour indicator
plt.figure(figsize=(50,50))
sns.heatmap(corr, linewidth=0.5)
##assigning the title for the map

plt.title("Qatar")
plt.savefig('plot5.png')
#display the figure
plt.show()


    




