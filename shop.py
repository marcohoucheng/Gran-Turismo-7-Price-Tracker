import pandas as pd

# build a db of where cars belong

def main():
    ## get full car list
    cars = pd.read_csv("https://raw.githubusercontent.com/ddm999/gt7info/web-new/_data/db/cars.csv")
    ## ./data/github_data/db/cars.csv
    cars = cars.rename({'ID': 'id', 'ShortName': 'Model'}, axis='columns')
    cars['id'] = cars['id'].astype(str)
    cars = cars.drop(['Model','Maker'], axis = 1)
    # cars['Maker'] = cars['Maker'].map(str)
    cars.set_index('id', inplace=True)

    central_db = pd.read_csv("https://raw.githubusercontent.com/ddm999/gt7info/web-new/_data/brandcentral/v112.csv")
    central_db['id'] = central_db['id'].astype(str)
    central_db.set_index('id', inplace=True)

    legend_db = pd.read_csv("./data/legend_historic.csv")
    legend_db['id'] = legend_db['id'].astype(str)
    legend_db.set_index('id', inplace=True)
    cols = legend_db.columns.tolist()
    legend_db[cols[3:-3]] = legend_db[cols[3:-3]].astype('Int64')

    used_db = pd.read_csv("./data/used_historic.csv")
    used_db['id'] = used_db['id'].astype(str)
    used_db.set_index('id', inplace=True)
    cols = used_db.columns.tolist()
    used_db[cols[3:-3]] = used_db[cols[3:-3]].astype('Int64')

    ## add 3 columns (for 3 shops) and flag which store they belong to
    cars['legend'] = cars.index.isin(legend_db.index)
    cars['used'] = cars.index.isin(used_db.index)
    cars['central'] = ( ~cars['legend'] & ~cars['used'] ) | cars.index.isin(central_db.index)

    pd.DataFrame.from_dict(cars).to_csv("./data/" + "shop.csv")
    print("DB created for shop information.\n")
    return 0

if __name__ == "__main__":
   main()