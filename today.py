# Script to simply return the available items in shops today.

import urllib.request, json, os, sys, datetime
import pandas as pd

def today(shop, data, new_data_only):

    shop_data = pd.DataFrame.from_dict(data[shop]['cars'])

    if new_data_only:
        shop_data = shop_data[shop_data['new'] == 'True']
    
    shop_data = shop_data.sort_values(by=['manufacturer', 'name'])

    if len(shop_data) == 0:
        print("\nNo new items available in", shop, "shop.\n")
        return 0

    print("\nAvailable in", shop, "shop:\n")

    for _, row in shop_data.iterrows():
        if row['state'] == 'soldout':
            continue
        elif row['state'] == 'limited':
            print(row['manufacturer'], row['name'], ":", row['credits'], "cr. (Leaving Soon)")
        elif row['new'] == 'True':
            print(row['manufacturer'], row['name'], ":", row['credits'], "cr. (New)")
        else:
            print(row['manufacturer'], row['name'], ":", row['credits'], "cr.")

def main():

    if len(sys.argv) == 1:
        new_data_only = False
    else:
        new_data_only = sys.argv[1] == 'new'

    date_format = '%y-%m-%d'

    url = urllib.request.urlopen("https://ddm999.github.io/gt7info/data.json")
    data = json.load(url)

    # Time stamp for latest data
    timestamp_date = data['updatetimestamp'][2:10]

    if datetime.datetime.strptime(timestamp_date, date_format).date() < datetime.date.today():
        print("\nToday's data is not available yet. The latest data is from", timestamp_date, "\n")
    else:
        print("\nToday's data is available.\n")

    today('legend', data, new_data_only)
    today('used', data, new_data_only)

if __name__ == "__main__":
    main()