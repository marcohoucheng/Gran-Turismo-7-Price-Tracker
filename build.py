import urllib.request, json, os, sys, datetime
import pandas as pd

if len(sys.argv) > 2:
    print("Too many arguments. Please specify the shop name as an argument. Default is 'legend'.")
    sys.exit(1)

if len(sys.argv) == 1:
   shop = 'legend'
else:
   shop = sys.argv[1]

# legend or used shop
shop = 'legend'

date_format = '%y-%m-%d'


todays_date = datetime.date.today().strftime(date_format)
path = "https://raw.githubusercontent.com/ddm999/gt7info/web-new/_data/" + shop + "/"
dir = [] # Initialize a list to store the dates from today back to 22-03-03

# Set the start and end dates
start_date = datetime.date(2022, 3, 3)
end_date = datetime.date.today()

# Iterate through the dates from start_date to end_date
while start_date <= end_date:
   # Include extension
   file = start_date.strftime(date_format) + ".csv"
   # Append the file name to the list
   dir.append(file)
   # Add one day to the start_date
   start_date += datetime.timedelta(days=1)

for i, file in enumerate(sorted(dir, reverse=True)):
   file_name = file[:-4]
   local_path = path + file
   tmp_df = pd.read_csv(local_path)
   tmp_df[tmp_df['state'] != 'soldout']
   tmp_df['id'] = tmp_df['id'].map(str)
   tmp_df.set_index('id', inplace=True)
   # tmp_df['cr'] = tmp_df['cr'].map(int)
   tmp_df = tmp_df.rename({'cr': file_name}, axis='columns')
   if file_name == todays_date:
      master_db = tmp_df[[file_name]]
   else:
      master_db = pd.merge(master_db, tmp_df[[file_name]], how='outer', left_index=True, right_index=True)# .sort_index()
   print("{0:0.1f}".format((i+1)/len(dir)*100), "% loaded", end="\r")

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

master_db = pd.merge(master_db, cars, how='left', left_index=True, right_index=True)
master_db = pd.merge(master_db, makers, how='left', left_on='Maker', right_index=True)
master_db = pd.merge(master_db, countries, how='left', left_on='Country Code', right_index=True)

cols = master_db.columns.tolist()
cols = ['Country', 'Manufacturer', 'Model'] + cols[:-6] + ['Country Short', 'Maker', 'Country Code']
master_db = master_db[cols]
master_db = master_db.sort_values(by=['Manufacturer'])

export_file = shop + "_historic.csv"
pd.DataFrame.from_dict(master_db).to_csv("export_file")
print("DB created.\n")