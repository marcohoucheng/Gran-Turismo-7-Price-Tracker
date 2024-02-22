# Create table for cars' metadata

import pandas as pd

def main():
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

    cars = pd.merge(cars, makers, how='left', left_on='Maker', right_index=True)
    cars = cars[['Manufacturer', 'Model']].sort_values(by=['Manufacturer', 'Model'])

    pd.DataFrame.from_dict(cars).to_csv("./data/" + "cars.csv")
    print("DB created for cars metadata.\n")
    return 0

if __name__ == "__main__":
   main()