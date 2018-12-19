#%% 
# file import
import pandas as pd  
friday = pd.read_csv('~/pytong/data-cleaning/BlackFriday.csv')

#%%
# looking at the data
# table shape
print(friday.shape)

#%%
# first 10 rows
print(friday.head(10))
