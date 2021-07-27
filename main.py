
# main file for assignment
print("above displays location of file 'main.py' saved")
print("\n")

# Print "Hello" 3 times
for number in range(3):
    print("Hello")
print("\n")

# Importing Python Packages to use
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import io
import datetime as datetime
import method

# reusable function to print the unique values in a dataframe field
def reusable_print_unique_field_values(dataframe_name, column):
    for i in dataframe_name[column].unique():
        print(i)
    return

# Requesting an API "CBM03 - Detailed Daily Card Payments" from www.cso.ie
# request=requests.get('https://ws.cso.ie/public/api.jsonrpc?data=%7B%22jsonrpc%22:%222.0%22,%22method%22:%22PxStat.Data.Cube_API.ReadDataset%22,%22params%22:%7B%22class%22:%22query%22,%22id%22:%5B%5D,%22dimension%22:%7B%7D,%22extension%22:%7B%22pivot%22:null,%22codes%22:false,%22language%22:%7B%22code%22:%22en%22%7D,%22format%22:%7B%22type%22:%22CSV%22,%22version%22:%221.0%22%7D,%22matrix%22:%22CBM03%22%7D,%22version%22:%222.0%22%7D%')

response=requests.get('https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/CBM03/CSV/1.0/en')

print(response.status_code)

if response.status_code==200:
    print("Success, status code = 200")
else:
     print("Error, status code does not equal 200")

data = pd.read_csv("https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/CBM03/CSV/1.0/en", parse_dates=['Daily'])
print("*****  log position 1 get api file   *****")
print("")
print("head of dataframe 'data':")
print(data.head())
print(data['Daily'])
print("")
print("describe: dataframe 'data':")
print(data.describe())
print("")
print("column names of dataframe 'data':")
print(list(data.columns))
print("test1")

print(data.count())
print(len(data.index))

data_count = len(data.index)
print("test2")

if data_count > 300:
    print("\n Count of rows in dataframe > 300")
else:
    print("\n Count of rows in dataframe =< 300")

print(type(data['Daily']))
print("")
from datetime import datetime

#data_ind= data.set_index("Daily")
#data_monthly=data_ind.resample('M').sum()
print(data.head())

#data.groupby(pd.Grouper(freq='M'))
#print(data.head())
format_str = "%Y %B %d"
# data["Month"]=data[datetime.strptime(data['Daily'], format_str)]

#data['Month'] = data.apply(pd.to_datetime(data['Daily'], format=format_str), axis=1)
# new_df = data[['Statistic',pd.to_datetime(data['Daily'], format=format_str),'Daily and Seven Day Rolling Totals','UNIT','VALUE']].copy()
new_df = data[['Statistic', 'Daily', 'Daily and Seven Day Rolling Totals', 'UNIT', 'VALUE']].copy()

print("*****  log position 2 create new_df   *****  ")

pd.options.display.max_colwidth = 100
print("head of dataframe 'new_df':")
print(new_df.head())
print("")
print("column names of dataframe 'new_df':")
print(list(new_df.columns))
print("")
print("return of first five rows of column 'Daily and Seven Day Rolling Totals' in dataframe df_new:")
print(new_df['Daily and Seven Day Rolling Totals'].head())
print("")
print("describe new_df:")
print(new_df.describe())
print("")
print("shape of new_df")
print(new_df.shape)

new_df_count = len(new_df.index)

if new_df_count == data_count:
    print("\n *** Check: Count of rows in new_df = count of rows in data")
else:
    print("\n *** Check: Count of rows in new_df does not equal count of rows in data")


print("")
print("display how many fields have not available:")
print(new_df.isna().sum())
print(" ")
print("replace nan with 0")
print("log position 3 before replace NaN with 0")

new_df2 = new_df.fillna({'VALUE': 0})
print("")
print("head of dataframe 'new_df2':")
print(new_df2.head())
print("")
print("check to ensure all fields have a value:")
print(new_df2.isna().sum())
print("log position 4 after replace NaN with 0")

print(list(new_df2.columns))

print("\n")
print("Example of reusable code:")
print('the unique values for "Statistic" field are:')
reusable_print_unique_field_values(new_df2, 'Statistic')
print("\n")
print('The unique values for "Daily and Seven Day Rolling Totals" field are:')
reusable_print_unique_field_values(new_df2, 'Daily and Seven Day Rolling Totals')
print("\n")

new_df3 = new_df2[new_df2["Daily and Seven Day Rolling Totals"] == "Daily total"]
print(new_df3)

#data_ind= data.set_index("Daily")
#data_monthly=data_ind.resample('M').sum()

#new_df3.set_index('Daily', inplace=True)
print("**********")
print(list(new_df3.columns))
print(new_df3.head())

# print unique values in "Statistic" field in dataframe using a for loop
for i in new_df3['Statistic'].unique():
    print(i)
print("*** loop   ***")


# the dataframe has a number of statistics included in the file, extract those relevant by creating a new df
# debit card transactions at AMT and POS level:
#Then merge two files together with pd.concat:
debit_card_trans_atm = new_df3[new_df3["Statistic"] == "Debit Card Transactions - ATM Withdrawals"]
debit_card_trans_pos = new_df3[new_df3["Statistic"] == "Debit Card Transactions - Point of Sale"]
debit_card_trans = pd.concat([debit_card_trans_atm, debit_card_trans_pos])

print(debit_card_trans_atm['Daily'])
print("\n")

debit_card_trans_atm_ind= debit_card_trans_atm.set_index("Daily")
debit_card_trans_atm_monthly=debit_card_trans_atm_ind.resample('M').sum()
print("monthly totals debit card atm trans:")
print(debit_card_trans_atm_monthly)
print("\n")
debit_card_trans_pos_ind= debit_card_trans_pos.set_index("Daily")
debit_card_trans_pos_monthly=debit_card_trans_pos_ind.resample('M').sum()
print("monthly totals debit card pos trans:")
print(debit_card_trans_pos_monthly)
print("\n")
debit_card_trans_ind= debit_card_trans.set_index("Daily")
debit_card_trans_monthly=debit_card_trans_ind.resample('M').sum()
print("monthly totals debit card trans:")
print(debit_card_trans_monthly)
print("\n")

#data_ind= data.set_index("Daily")
#data_monthly=data_ind.resample('M').sum()

# use of indexing and list
totals = ["Total value for Debit Card Transactions - ATM Withdrawals", "Total value for Debit Card Transactions - Point of Sales","Total value for Debit Card Transactions"]

print(totals[0],":", debit_card_trans_atm["VALUE"].sum())
print(totals[1],":", debit_card_trans_pos["VALUE"].sum())
print(totals[2],":", debit_card_trans["VALUE"].sum())

print("******indexing used above")

print(debit_card_trans_atm.shape)
print(debit_card_trans_pos.shape)
print(debit_card_trans.shape)
print(debit_card_trans.describe())

debit_card_vols_atm = new_df3[new_df3["Statistic"] == "Debit Card Volumes - ATM Withdrawals"]
debit_card_vols_pos = new_df3[new_df3["Statistic"] == "Debit Card Volumes - Point of Sale"]
debit_card_vols = pd.concat([debit_card_vols_atm, debit_card_vols_pos])

print(debit_card_vols_atm.shape)
print(debit_card_vols_pos.shape)
print(debit_card_vols.shape)

#Daily column contains daily date, need to group up to month level for analysis.
# set Daily to be index and then group up using resample with Month frequency and sum the VALUE column
debit_card_vols_atm_ind = debit_card_vols_atm.set_index("Daily")
debit_card_vols_atm_monthly = debit_card_vols_atm_ind.resample('M').sum()
print("monthly totals debit card volume atm:")
print(debit_card_vols_atm_monthly)
print("\n")
debit_card_vols_pos_ind= debit_card_vols_pos.set_index("Daily")
debit_card_vols_pos_monthly=debit_card_vols_pos_ind.resample('M').sum()
print("monthly totals debit card volume pos:")
print(debit_card_vols_pos_monthly)
print("\n")
debit_card_vols_ind= debit_card_vols.set_index("Daily")
debit_card_vols_monthly=debit_card_vols_ind.resample('M').sum()
print("monthly totals debit card volume:")
print(debit_card_vols_monthly)
print("\n")

debit_card_trans_test=pd.merge_ordered(debit_card_trans_atm_monthly, debit_card_trans_pos_monthly, on='Daily', suffixes=('_dc_trans_atm', '_dc_trans_pos'))
print(debit_card_trans_test)
debit_card_trans_monthly_merged=pd.merge_ordered(debit_card_trans_test, debit_card_trans_monthly, on='Daily', suffixes=('_dc_trans_atm', '_dc_trans_pos'))
debit_card_trans_monthly_merged.rename(columns = {'VALUE':'VALUE_dc_trans_total'}, inplace=True)
print(debit_card_trans_monthly_merged)

debit_card_vols_test=pd.merge_ordered(debit_card_vols_atm_monthly, debit_card_vols_pos_monthly, on='Daily', suffixes=('_dc_vols_atm', '_dc_vols_pos'))
print(debit_card_vols_test)
debit_card_vols_monthly_merged=pd.merge_ordered(debit_card_vols_test, debit_card_vols_monthly, on='Daily', suffixes=('_dc_vols_atm', '_dc_vols_pos'))
debit_card_vols_monthly_merged.rename(columns = {'VALUE':'VALUE_dc_vols_total'}, inplace=True)
print(debit_card_vols_monthly_merged)

debit_card_monthly_merged=pd.merge_ordered(debit_card_trans_monthly_merged, debit_card_vols_monthly_merged, on='Daily', suffixes=('__trans', '__vols'))
#debit_card_trans_monthly_merged.rename(columns = {'VALUE':'VALUE_dc_trans_total'}, inplace=True)
print(debit_card_monthly_merged)
print("column names of dataframe 'debit_card_monthly':")
print(list(debit_card_monthly_merged.columns))
print("merge test above***********")
print("\n")

#chart to show transaction and volume
fig, ax=plt.subplots(2,1, sharex=True)
ax[0].plot(debit_card_monthly_merged["Daily"], debit_card_monthly_merged["VALUE_dc_vols_atm"], marker="o", linestyle="--", color="green", label="ATM transactions")
ax[0].plot(debit_card_monthly_merged["Daily"], debit_card_monthly_merged["VALUE_dc_vols_pos"], marker="v", linestyle="--", color="cyan", label="POS transactions")
#ax[0].set_xlabel("Date")
ax[0].set_ylabel("Volume of Debit Card transactions")
ax[0].set_title("Volume of Debit Card transactions in Euro Thousand")

ax[1].plot(debit_card_monthly_merged["Daily"], debit_card_monthly_merged["VALUE_dc_trans_atm"], marker="o", linestyle="--", color="green", label="ATM transactions")
ax[1].plot(debit_card_monthly_merged["Daily"], debit_card_monthly_merged["VALUE_dc_trans_pos"], marker="v", linestyle="--", color="cyan", label="POS transactions")
ax[1].set_xlabel("Date")
ax[1].set_ylabel("Number of transactions")
ax[1].set_title("Number of Debit Card transactions")
plt.legend()
plt.show()
fig.savefig("debit_card_trans_vol.png")
print("\n")
print("*****  debit cards   *****")

#repeat same steps as for debit cards above:
#the dataframe has a number of statistics included in the file, extract those relevant by creating a new df
# debit card transactions at AMT and POS level:
#Then merge two files together with pd.concat:
credit_card_trans_per = new_df3[new_df3["Statistic"] == "Credit Card Transactions - Personal Cards"]
credit_card_trans_bus = new_df3[new_df3["Statistic"] == "Credit Card Transactions - Business Cards"]
credit_card_trans = pd.concat([credit_card_trans_per, credit_card_trans_bus])

print(credit_card_trans_per.shape)
print(credit_card_trans_bus.shape)
print(credit_card_trans.shape)
print(credit_card_trans.describe())

credit_card_vols_per = new_df3[new_df3["Statistic"] == "Credit Card Volumes - Personal Cards"]
credit_card_vols_bus = new_df3[new_df3["Statistic"] == "Credit Card Volumes - Business Cards"]
credit_card_vols = pd.concat([credit_card_vols_per, credit_card_vols_bus])

#credit_card_trans_per.set_index("Daily")
#credit_card_trans_per["Month"] = credit_card_trans_per.index.resample('M')

print("test monthly conversion********************")
#Daily column contains daily date, need to group up to month level for analysis.
# set Daily to be index and then group up using resample with Month frequency and sum the VALUE column
credit_card_trans_per_ind = credit_card_trans_per.set_index("Daily")
credit_card_trans_per_monthly = credit_card_trans_per_ind.resample('M').sum()
print("monthly totals credit card trans per:")
print(credit_card_trans_per_monthly)
print("\n")
credit_card_trans_bus_ind = credit_card_trans_bus.set_index("Daily")
credit_card_trans_bus_monthly = credit_card_trans_bus_ind.resample('M').sum()
print("monthly totals credit card trans bus:")
print(credit_card_trans_bus_monthly)
print("\n")
credit_card_trans_ind = credit_card_trans.set_index("Daily")
credit_card_trans_monthly = credit_card_trans_ind.resample('M').sum()
print("monthly totals credit card trans:")
print(credit_card_trans_monthly)
print("\n")

credit_card_trans_test=pd.merge_ordered(credit_card_trans_per_monthly, credit_card_trans_bus_monthly, on='Daily', suffixes=('_cc_trans_per', '_cc_trans_bus'))
print(credit_card_trans_test)
credit_card_trans_monthly_merged=pd.merge_ordered(credit_card_trans_test, credit_card_trans_monthly, on='Daily', suffixes=('_cc_trans_per', '_cc_trans_bus', '_cc_trans_total'))
credit_card_trans_monthly_merged.rename(columns = {'VALUE':'VALUE_cc_trans_total'}, inplace=True)
print(credit_card_trans_monthly_merged)
print("merge test above***********")
print("\n")

credit_card_vols_per_ind= credit_card_vols_per.set_index("Daily")
credit_card_vols_per_monthly=credit_card_vols_per_ind.resample('M').sum()
print("monthly totals credit card per vols:")
print(credit_card_vols_per_monthly)
print("\n")
credit_card_vols_bus_ind= credit_card_vols_bus.set_index("Daily")
credit_card_vols_bus_monthly=credit_card_vols_bus_ind.resample('M').sum()
print("monthly totals credit card bus vols:")
print(credit_card_vols_bus_monthly)
print("\n")
credit_card_vols_ind= credit_card_vols.set_index("Daily")
credit_card_vols_monthly=credit_card_vols_ind.resample('M').sum()
print("monthly totals credit card vols:")
print(credit_card_vols_monthly)
print("\n")

credit_card_vols_test=pd.merge_ordered(credit_card_vols_per_monthly, credit_card_vols_bus_monthly, on='Daily', suffixes=('_cc_vols_per', '_cc_vols_bus'))
print(credit_card_vols_test)
credit_card_vols_monthly_merged=pd.merge_ordered(credit_card_vols_test, credit_card_vols_monthly, on='Daily', suffixes=('_cc_vols_per', '_cc_vols_bus', '_cc_vols_total'))
credit_card_vols_monthly_merged.rename(columns = {'VALUE':'VALUE_cc_vols_total'}, inplace=True)
print(credit_card_vols_monthly_merged)

credit_card_monthly_merged=pd.merge_ordered(credit_card_trans_monthly_merged, credit_card_vols_monthly_merged, on='Daily', suffixes=('__trans', '__vols'))
#credit_card_trans_monthly_merged.rename(columns = {'VALUE':'VALUE_cc_trans_total'}, inplace=True)
print(credit_card_monthly_merged)
print("column names of dataframe 'retail_sales':")
print(list(credit_card_monthly_merged.columns))
print("merge test above***********")
print("\n")

print(credit_card_vols_per.shape)
print(credit_card_vols_bus.shape)
print(credit_card_vols.shape)

#fig, ax=plt.subplots(2,1)
ax[0].plot(debit_card_monthly_merged["Daily"], debit_card_monthly_merged["VALUE_dc_vols_atm"], marker="o", linestyle="--", color="r", label="ATM transactions")
ax[0].plot(debit_card_monthly_merged["Daily"], debit_card_monthly_merged["VALUE_dc_vols_pos"], marker="v", linestyle="--", color="b", label="POS transactions")
ax[0].set_xlabel("Date")
ax[0].set_ylabel("Volume of Debit Card transactions")
ax[0].set_title("Volume of Debit Card transactions in Euro Thousand")

ax[1].plot(debit_card_monthly_merged["Daily"], debit_card_monthly_merged["VALUE_dc_trans_atm"], marker="o", linestyle="--", color="r", label="ATM transactions")
ax[1].plot(debit_card_monthly_merged["Daily"], debit_card_monthly_merged["VALUE_dc_trans_pos"], marker="v", linestyle="--", color="b", label="POS transactions")
ax[1].set_xlabel("Date")
ax[1].set_ylabel("Number of transactions")
ax[1].set_title("Number of Debit Card transactions")
#plt.legend()
#plt.show()

fig, ax=plt.subplots(2,1, sharex=True)
ax[0].plot(credit_card_monthly_merged["Daily"], credit_card_monthly_merged["VALUE_cc_vols_per"], marker="o", linestyle="--", color="r", label="Personal volume")
ax[0].plot(credit_card_monthly_merged["Daily"], credit_card_monthly_merged["VALUE_cc_vols_bus"], marker="v", linestyle="--", color="b", label="Business volume")
#ax[1].set_xlabel("Date")
ax[0].set_ylabel("Volume of transactions")
ax[0].set_title("Volume of Credit Card transactions in Euro Thousand")

ax[1].plot(credit_card_monthly_merged["Daily"], credit_card_monthly_merged["VALUE_cc_trans_per"], marker="o", linestyle="--", color="r", label="Personal transactions")
ax[1].plot(credit_card_monthly_merged["Daily"], credit_card_monthly_merged["VALUE_cc_trans_bus"], marker="v", linestyle="--", color="b", label="Business transactions")
ax[1].set_xlabel("Date")
ax[1].set_ylabel("Number of transactions")
ax[1].set_title("Number of Credit Card transactions")
plt.legend()
fig.savefig("credit_card_trans_vol.png")

plt.show()

print("*****  credit cards   *****")

# daily_card_payments= new_df2.sort_values("Daily and Seven Day Rolling =Totals", ascending=[True])
# print(daily_card_payments.head())

# mask_rolling_totals = daily_card_payments.'Daily and Seven Day Rolling Totals' == 'Daily total'
# daily_total = daily_card_payments.loc[mask_rolling_totals]
# daily_total.describe(include='object')


print("\n")

print("Detailed Daily Card Payments file imported")

# import Retail Sales Index in csv file from CSO website call 'retail_sales' dataframe
# hardcoded filename without path
retail_sales = pd.read_csv("retail_sales_index_cso.csv")

print("*****  log position 5 read retail sales csv file   *****")

# Look at retail_sales

print(retail_sales.head())
print("")
print("column names of dataframe 'retail_sales':")
print(list(retail_sales.columns))
print("n/")
print("shape dataframe 'retail_sales':")
print(retail_sales.shape)
print("")
print("mapping for retail_sales")
print("")
# hardcoded filename without path
mapping = pd.read_csv("mapping.csv")
print(mapping.info())
print("*****  log position 6 read csv mapping   *****")

#iterrow example to print mapping reference table
for index, row in mapping.iterrows():
    print(row['C02583V03135'], row['NACE higher Group'])

#print(mapping)
print("")
new_retail_sales = retail_sales.merge(mapping, on=['C02583V03135'])
new_retail_sales.sort_values("TLIST(M1)", ascending=[True])
print("")
print("*****  log position 7 sorting     *****")

print(new_retail_sales.isna().sum())
print(new_retail_sales.head())
print(list(new_retail_sales.columns))
print("describe")
print(new_retail_sales.describe(include='all'))

# create new df extract of retail_sales with date greater than 2019
retail_sales_20_21 = new_retail_sales[new_retail_sales['TLIST(M1)'] > 201912].copy()
retail_sales_20_21_grouped = retail_sales_20_21.sort_values("NACE higher Group")
print("")
print("*****  log position 8 filter retail sales file > 2019     *****")
retail_sales_20_21_grouped.drop(columns=['Month', 'NACE Group', 'UNIT'],
                        axis=1,
                        inplace=True)
print(list(retail_sales_20_21_grouped.columns))
print("")
print("log position 9 drop columns from df")
print(retail_sales_20_21_grouped.head())
print("describe below:")
print(retail_sales_20_21_grouped.describe())
print(retail_sales_20_21_grouped.shape)
print("position 10")

# List
year_value = ["FY 2020 totals value", "YTD 2021 totals value"]
print(year_value)
year2020 = retail_sales_20_21[retail_sales_20_21['TLIST(M1)'] < 202101]["VALUE"].agg('sum')
year2021 = retail_sales_20_21[retail_sales_20_21['TLIST(M1)'] > 201912]["VALUE"].agg('sum')
print("\n")

# tidy up
print(year_value[0])
print(year2020)

print(year_value[1])
print(year2021)
print("\n")

retail_sales_20_21_grouped = retail_sales_20_21.groupby(["TLIST(M1)", "NACE higher Group"])["VALUE"].agg('sum').copy()
print(retail_sales_20_21_grouped)
print("**** Grouping used above")
print("\n")
print("position 11 group df with date and higher NACE code")

#not working!
# set TLIST(M1) to be index and then group up using resample with Month frequency and sum the VALUE column
#retail_sales_20_21_grouped_ind = retail_sales_20_21_grouped.set_index("TLIST(M1)")
#retail_sales_20_21_grouped_monthly = retail_sales_20_21_grouped_ind.resample('M').sum()

#retail_sales_20_21_grouped_monthly.plot(kind='bar', y='VALUE')
#plt.show()
# retail_sales_20_21.groupby(["TLIST(M1),"NACE higher Group"])["VALUE"].agg('sum').plot(kind='bar', y='VALUE')


numpy_df = pd.read_csv("retail_sales_index_cso.csv", usecols = ["Statistic"]) # read just the Statistic field from the csv file
#convert dataframe to numpy array
arr = numpy_df.to_numpy()
print (arr.size)  # print count of values in numpy array
print(np.unique(arr)) # print unique numpy array values