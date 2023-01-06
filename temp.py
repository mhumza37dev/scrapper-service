import pandas as pd
url='https://github.com/owid/covid-19-data/blob/master/public/data/latest/owid-covid-latest.csv'
df=pd.read_csv(url, sheet_name='Sheet1')
print(df)
