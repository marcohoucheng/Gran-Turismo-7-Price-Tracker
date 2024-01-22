import urllib.request, json, os, sys, datetime
import pandas as pd

## TO DO
# Replace 'legend' with a shop variable

# Testing script
test = False

# legend or used shop
shop = 'legend'

date_format = '%y-%m-%d'

# Need to write a code to check we have today's data
if test:
   # newest file in local directory
   todays_date = '24-01-15'
   path = "./github_data/" + shop + "/"
   dir = os.listdir(path)
else:
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
      legend_db = tmp_df[[file_name]]
   else:
      legend_db = pd.merge(legend_db, tmp_df[[file_name]], how='outer', left_index=True, right_index=True)# .sort_index()
   print("{0:0.1f}".format((i+1)/len(dir)*100), "% loaded", end="\r")

if test:
   cars = pd.read_csv("./github_data/db/cars.csv")
   makers = pd.read_csv("./github_data/db/maker.csv")
   countries = pd.read_csv("./github_data/db/country.csv")
else:
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

legend_db = pd.merge(legend_db, cars, how='left', left_index=True, right_index=True)
legend_db = pd.merge(legend_db, makers, how='left', left_on='Maker', right_index=True)
legend_db = pd.merge(legend_db, countries, how='left', left_on='Country Code', right_index=True)

cols = legend_db.columns.tolist()
cols = ['Country', 'Manufacturer', 'Model'] + cols[:-6] + ['Country Short', 'Maker', 'Country Code']
legend_db = legend_db[cols]
legend_db = legend_db.sort_values(by=['Manufacturer'])

pd.DataFrame.from_dict(legend_db).to_csv("legend_historic.csv")
print("DB created.\n")