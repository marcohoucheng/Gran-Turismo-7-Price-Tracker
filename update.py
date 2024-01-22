import urllib.request, json, os, sys, datetime
import pandas as pd

## TO DO
# Replace 'legend' with a shop variable
# Improve implementation of adding missing car information

test = False

date_format = '%y-%m-%d'

url = urllib.request.urlopen("https://ddm999.github.io/gt7info/data.json")
new_data = json.load(url)

# Time stamp for latest data
timestamp_date = new_data['updatetimestamp'][2:10]

new_data = pd.DataFrame.from_dict(new_data['legend']['cars'])

# load db
legend_db = pd.read_csv('legend_historic.csv')
legend_db['id'] = legend_db['id'].map(str)
legend_db.set_index('id', inplace=True)
cols = legend_db.columns.tolist()

# testing: drop today's data if exist in db
if test:
    legend_db.drop(timestamp_date, 'columns', inplace = True, errors='ignore')

# timestamp check
latest_recorded_date = cols[3]
# if timestamp is the same or older than the recorded date, exit
if datetime.datetime.strptime(timestamp_date, date_format) < datetime.datetime.strptime(latest_recorded_date, date_format):
    print("No new data available.\nExiting...")
    sys.exit(0)
elif datetime.datetime.strptime(timestamp_date, date_format) == datetime.datetime.strptime(latest_recorded_date, date_format):
    print("Today's data not available yet. Please try again later.\nExiting...")
    sys.exit(0)
elif (datetime.datetime.strptime(timestamp_date, date_format) - datetime.datetime.strptime(latest_recorded_date, date_format)).days > 1:
    # missing more than one day of data, need to dig from github...
    print("Last updated on", latest_recorded_date, ".")
    print("Missing data for", (datetime.datetime.strptime(timestamp_date, date_format) - datetime.datetime.strptime(latest_recorded_date, date_format)).days, "days.")
    start_date = datetime.datetime.strptime(latest_recorded_date, date_format) + datetime.timedelta(days=1)
    end_date = datetime.datetime.strptime(timestamp_date, date_format)
    dates = []
    # Loop through the dates
    while start_date <= end_date:
        # Get the data and join to the db
        # Get the string of start_date
        start_date_str = start_date.strftime(date_format)
        # Gget a list of dates looped through
        dates.insert(0, start_date_str)
        # Get the data from github
        path = "https://raw.githubusercontent.com/ddm999/gt7info/web-new/_data/" + "legend" + "/" + start_date_str + ".csv"
        tmp_df = pd.read_csv(path)
        # Clean the data
        tmp_df[tmp_df['state'] != 'soldout']
        tmp_df['id'] = tmp_df['id'].map(str)
        tmp_df.set_index('id', inplace=True)
        tmp_df = tmp_df.rename({'cr': start_date_str}, axis='columns')
        # Outer join to the db
        legend_db = pd.merge(legend_db, tmp_df[[start_date_str]], how='outer', left_index=True, right_index=True)
        # Add one day to the start_date
        start_date += datetime.timedelta(days=1)
    # Rearrange the columns
    cols = ['Country', 'Manufacturer', 'Model'] + dates + cols[3:]
    legend_db = legend_db[cols]
    # Check timestamp date is today's date, if not then print warning message
    if datetime.datetime.strptime(timestamp_date, date_format).date() < datetime.datetime.today().date():
        print("Today's data not available yet. DB updated up to yesterday's data.\nExiting...")
else:
    new_data = new_data.rename({'carid': 'id', 'credits': timestamp_date}, axis='columns')
    new_data.set_index('id', inplace=True)
    new_data = new_data[[timestamp_date]]

    legend_db = pd.merge(legend_db, new_data, how='outer', left_index=True, right_index=True)

    cols = ['Country', 'Manufacturer', 'Model'] + [timestamp_date] + cols[3:]
    legend_db = legend_db[cols]

# check if car information has been added
# id's of missing car information
is_missing_info = legend_db['Model'].isnull()
if sum(is_missing_info) > 0:
    cars = pd.read_csv("https://raw.githubusercontent.com/ddm999/gt7info/web-new/_data/db/cars.csv")
    makers = pd.read_csv("https://raw.githubusercontent.com/ddm999/gt7info/web-new/_data/db/maker.csv")
    countries = pd.read_csv("https://raw.githubusercontent.com/ddm999/gt7info/web-new/_data/db/country.csv")

    cars = cars.rename({'ID': 'id', 'ShortName': 'Model'}, axis='columns')
    cars['id'] = cars['id'].map(str)
    cars['Maker'] = cars['Maker'].map(str)
    cars.set_index('id', inplace=True)

    makers = makers.rename({'ID': 'id', 'Name': 'Manufacturer', 'Country': 'Country Code'}, axis='columns')
    makers['id'] = makers['id'].map(str)
    makers['Country Code'] = makers['Country Code'].map(str)
    makers.set_index('id', inplace=True)

    countries = countries.rename({'ID': 'id', 'Name': 'Country', 'Code': 'Country Short'}, axis='columns')
    countries['id'] = countries['id'].map(str)
    countries.set_index('id', inplace=True)

    # remove existing columns
    legend_db = legend_db.drop(['Country', 'Manufacturer', 'Model', 'Country Short', 'Maker', 'Country Code'], axis=1)

    legend_db = pd.merge(legend_db, cars, how='left', left_index=True, right_index=True)
    legend_db = pd.merge(legend_db, makers, how='left', left_on='Maker', right_index=True)
    legend_db = pd.merge(legend_db, countries, how='left', left_on='Country Code', right_index=True)

    cols = legend_db.columns.tolist()
    cols = ['Country', 'Manufacturer', 'Model'] + cols[:-6] + ['Country Short', 'Maker', 'Country Code']
    legend_db = legend_db[cols]

legend_db = legend_db.sort_values(by=['Manufacturer'])
pd.DataFrame.from_dict(legend_db).to_csv("legend_historic.csv")
print("DB updated.\n")