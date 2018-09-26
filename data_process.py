import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('C:/Users/sunshine/Desktop/oridata.csv')
#print ("缺失值数量")
#print(df.shape[0]- df.count())  #统计缺失值数量
#print ("缺失值比例")
#print(1 - df.count()/df.shape[0]) #统计缺失值比例
#df = df.drop('Cabin', axis=1)
#print(df.channelGrouping.value_counts())

df.loc[df["channelGrouping"]=="Organic Search","channelGrouping"] =1

df.loc[df["channelGrouping"]=="Social","channelGrouping"] =2

df.loc[df["channelGrouping"]=="Direct","channelGrouping"] =3

df.loc[df["channelGrouping"]=="Referral","channelGrouping"] =4

df.loc[df["channelGrouping"]=="Paid Search","channelGrouping"] =5

df.loc[df["channelGrouping"]=="Affiliates","channelGrouping"] =6

df.loc[df["channelGrouping"]=="Display","channelGrouping"] =7

df["channelGrouping"].fillna('0')

print(df.channelGrouping.value_counts())

