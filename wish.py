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

tab = pd.merge(cars, makers, how='left', left_on='Maker', right_index=True)
tab = tab[['Manufacturer', 'Model']].sort_values(by=['Manufacturer', 'Model'])

# Provide a search list for users to select (multiple cars)
# Store the list of cars ID
# Separate these IDs into 3 tables (Central, Legend, Used)
# Get latest price, when it was last in shops, and estimate days
# Create a markdown?