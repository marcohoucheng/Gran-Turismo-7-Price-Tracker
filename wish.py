import urllib.request, json, os, sys, datetime
import pandas as pd

# Build the car -> ID table
cars = pd.read_csv("https://raw.githubusercontent.com/ddm999/gt7info/web-new/_data/db/cars.csv")
makers = pd.read_csv("https://raw.githubusercontent.com/ddm999/gt7info/web-new/_data/db/maker.csv")

cars = cars.rename({'ID': 'id', 'ShortName': 'Model'}, axis='columns')
cars['id'] = cars['id'].map(str)
cars['Maker'] = cars['Maker'].map(str)
cars.set_index('id', inplace=True)

makers = makers.rename({'ID': 'id', 'Name': 'Manufacturer', 'Country': 'Country Code'}, axis='columns')
makers['id'] = makers['id'].map(str)
makers['Country Code'] = makers['Country Code'].map(str)
makers.set_index('id', inplace=True)

cars = cars.merge(makers, how='left', left_index=True, right_index=True)

cols = master_db.columns.tolist()
cols = ['Country', 'Manufacturer', 'Model'] + cols[:-6] + ['Country Short', 'Maker', 'Country Code']
master_db = master_db[cols]
master_db = master_db.sort_values(by=['Country', 'Manufacturer', 'Model'])

pd.DataFrame.from_dict(master_db).to_csv("./data/" + shop + "_historic.csv")
print("DB created for", shop, "shop \n")

# Provide a search list for users to select (multiple cars)
# Store the list of cars ID
# Separate these IDs into 3 tables (Central, Legend, Used)
# Get latest price, when it was last in shops, and estimate days
# Create a markdown?