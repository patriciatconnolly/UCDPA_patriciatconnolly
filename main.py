# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# Importing Python Packages to use
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Requesting an API "CBM03 - Detailed Daily Card Payments" from www.cso.ie
request=requests.get('https://ws.cso.ie/public/api.jsonrpc?data=%7B%22jsonrpc%22:%222.0%22,%22method%22:%22PxStat.Data.Cube_API.ReadDataset%22,%22params%22:%7B%22class%22:%22query%22,%22id%22:%5B%5D,%22dimension%22:%7B%7D,%22extension%22:%7B%22pivot%22:null,%22codes%22:false,%22language%22:%7B%22code%22:%22en%22%7D,%22format%22:%7B%22type%22:%22CSV%22,%22version%22:%221.0%22%7D,%22matrix%22:%22CBM03%22%7D,%22version%22:%222.0%22%7D%7D')

print(request.status_code)

print(request.text)

print(request.json())

parsed_data=request.json()

print(parsed_data["id"])

for i in parsed_data:
        print(i["id"])
#pd.DataFrame=request.json()
print('here1')
#data=pd.DataFrame

