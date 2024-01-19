import urllib.request, json, os, sys, datetime
import pandas as pd

test = True

url = urllib.request.urlopen("https://ddm999.github.io/gt7info/data.json")
new_data = json.load(url)

# Time stamp for latest data
todays_date = new_data['updatetimestamp'][2:10]

new_data = pd.DataFrame.from_dict(new_data['legend']['cars'])

# load db
legend_db = pd.read_csv('legend_historic.csv')
legend_db['id'] = legend_db['id'].map(str)
legend_db.set_index('id', inplace=True)

# if timestamp is the same or older than the recorded date, exit

if test:
    legend_db.drop(todays_date, 'columns', inplace = True, errors='ignore')


new_data = new_data.rename({'carid': 'id', 'credits': todays_date}, axis='columns')
new_data.set_index('id', inplace=True)
new_data = new_data[[todays_date]]

legend_db = pd.merge(legend_db, new_data, how='outer', left_index=True, right_index=True)

cols = legend_db.columns.tolist()
cols = ['Country', 'Manufacturer', 'Model'] + cols[-1:] + cols[3:-1]
legend_db = legend_db[cols]
legend_db = legend_db.sort_values(by=['Manufacturer'])

# check if car information has been added