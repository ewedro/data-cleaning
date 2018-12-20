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

#%%
# let's look at column types
print(friday.dtypes)

#%% 
# learn some more about purchase price
purch = friday["Purchase"]
print(purch.describe())

#%%
# take a look at row with purchase with highest price
highest_purch = friday.loc[friday["Purchase"]==23961]
print(highest_purch)

#%% 
# exploring Age column
age = friday["Age"]
print(age.value_counts())

#%%
# take a look at the same column but with gender split
# females
age_female = friday.loc[friday["Gender"]=="F","Age"]
print(age_female.value_counts())

#%%
#males
age_male = friday.loc[friday["Gender"]=="M","Age"]
print(age_male.value_counts())

#%%
# number of purchases made by females
print(age_female.shape)

#%%
# number of purchases made by males
print(age_male.shape)

#%%
# checking percentage of women
tot_fem = float(age_female.shape[0])
print(tot_fem)
tot_mal = float(age_male.shape[0])
print(tot_mal)
tot_gen = tot_fem + tot_mal
fem_perc = tot_fem/tot_gen*100
print(fem_perc)

#%%
# checking percentage of men
mal_perc = tot_mal/tot_gen*100
print(mal_perc)

#%%
# ## it looks like 3 times more man than women made purchases during black friday 

