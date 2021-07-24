# main file for assignment

# Importing Python Packages to use

import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import io

# Requesting an API "CBM03 - Detailed Daily Card Payments" from www.cso.ie
#request=requests.get('https://ws.cso.ie/public/api.jsonrpc?data=%7B%22jsonrpc%22:%222.0%22,%22method%22:%22PxStat.Data.Cube_API.ReadDataset%22,%22params%22:%7B%22class%22:%22query%22,%22id%22:%5B%5D,%22dimension%22:%7B%7D,%22extension%22:%7B%22pivot%22:null,%22codes%22:false,%22language%22:%7B%22code%22:%22en%22%7D,%22format%22:%7B%22type%22:%22CSV%22,%22version%22:%221.0%22%7D,%22matrix%22:%22CBM03%22%7D,%22version%22:%222.0%22%7D%7D')

#request=requests.get('https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/CBM03/CSV/1.0/en')

#print(request.status_code)

#if request.status_code==200:
 #       print("Success")
#else:
 #       print("Error")

data=pd.read_csv("https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/CBM03/CSV/1.0/en")
print(data.head())
print(data.describe())
print(list(data.columns))

new_df = data[['Statistic','Daily','Daily and Seven Day Rolling Totals','UNIT','VALUE']].copy()

pd.options.display.max_colwidth=100

print(new_df.head())
print(list(new_df.columns))
print(new_df['Daily and Seven Day Rolling Totals'].head())
print(new_df.describe())
print(new_df.shape)
print(new_df.isna().sum())

print("replace nan with 0")

new_df2=new_df.fillna(0)
print(new_df2.head())
print(new_df2.isna().sum())

#print(request.text)
#df=pd.read_csv(io.StringIO(request.text))
#print(df.head())


#print("Detailed Daily Card Payments file imported")

#retail_sales=pd.read_csv("retail_sales_index_cso.csv")

# Look at retail_sales
#print(retail_sales.head())