import pandas as pd
houses = pd.read_csv('thads2013n.txt')
house_shape = houses.shape
print(house_shape)
print(houses.head(20))
print(houses.info())
print(houses.columns)

houses.rename({"AGE1":"age","LMED":"area_avg_income","FMR":"avg_market_rent"}, axis=1, inplace=True)
print(houses.iloc[:10,:10])



#print(houses['AGE1'].unique())
#print('there is some data with -9 age value')
#print(houses[houses['AGE1']==-9])