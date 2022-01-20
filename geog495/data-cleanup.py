import pandas as pd
import numpy as np

data = pd.read_csv('spd_2020.csv')
wData = data.iloc[0:10, ].sort_values('total_dispatches', ascending=False)
nData = data.iloc[10:22, ].sort_values('total_dispatches', ascending=False)
swData = data.iloc[22:36, ].sort_values('total_dispatches', ascending=False)
eData = data.iloc[36:46, ].sort_values('total_dispatches', ascending=False)
sData = data.iloc[46:63, ].sort_values('total_dispatches', ascending=False)
finalData = pd.concat([wData, nData, swData, eData, sData])
finalData.to_csv('cleaned_2020.csv')