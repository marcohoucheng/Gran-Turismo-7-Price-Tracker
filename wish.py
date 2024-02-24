import urllib.request, json, os, sys, datetime
import pandas as pd
import update

def main():
    update.main()

    # list of cars from the game, should be a user input
    wish = [216,773,810,1565,1984,2167,3362]
    wish = pd.DataFrame(wish).astype(str)

    today_shop = []
    past_shop = []

    shops = pd.read_csv("./data/shop.csv")
    shops['id'] = shops['id'].astype(str)
    shops.set_index('id', inplace=True)

    # Check if the cars are in the shops
    wish_used = wish[wish.isin(shops[shops['used']].index)].dropna()
    wish_legend = wish[wish.isin(shops[shops['legend']].index)].dropna()

    cars = pd.read_csv("./data/cars.csv")
    cars['id'] = cars['id'].astype(str)
    cars.set_index('id', inplace=True)

    ## Legend

    # load legend db
    if not(os.path.exists("./data/legend_historic.csv")):
        print("legend shop DB not found in the data folder.\nPlease run build.py to create a new DB.")
        return 0

    legend_db = pd.read_csv("./data/legend_historic.csv")
    legend_db['id'] = legend_db['id'].astype(str)
    legend_db.set_index('id', inplace=True)
    cols = legend_db.columns.tolist()
    legend_db[cols[3:-3]] = legend_db[cols[3:-3]].astype('Int64')

    for car in range(wish_legend.size):
        car_id = wish_legend[0].tolist()[car]
        car_info = cars.loc[car_id]
        prices = legend_db.loc[[car_id]].dropna(axis=1, how='all')
        last_avail = prices.columns.tolist()[3]
        if last_avail == datetime.date.today().strftime("%y-%m-%d"):
            today_shop.append([car_info[0] + " " + car_info[1], int(prices[last_avail]), "Legend"])
            # print(car_info[0] + " " + car_info[1], " is in the shop today at price", int(prices[last_avail]), "cr.")
        else:
            past_shop.append([car_info[0] + " " + car_info[1], last_avail, int(prices[last_avail]), "Legend"])
            # print(car_info[0] + " " + car_info[1], " was last in the legend shop on " + last_avail + " at price", int(prices[last_avail]), "cr.")


    ## Used
    # load used db
    if not(os.path.exists("./data/used_historic.csv")):
        print("legend shop DB not found in the data folder.\nPlease run build.py to create a new DB.")
        return 0

    used_db = pd.read_csv("./data/used_historic.csv")
    used_db['id'] = used_db['id'].astype(str)
    used_db.set_index('id', inplace=True)
    cols = used_db.columns.tolist()
    used_db[cols[3:-3]] = used_db[cols[3:-3]].astype('Int64')
    
    for car in range(wish_used.size):
        car_id = wish_used[0].tolist()[car]
        car_info = cars.loc[car_id]
        prices = used_db.loc[[car_id]].dropna(axis=1, how='all')
        last_avail = prices.columns.tolist()[3]
        
        if last_avail == datetime.date.today().strftime("%y-%m-%d"):
            today_shop.append([car_info[0] + " " + car_info[1], int(prices[last_avail]), "Used"])
            # print(car_info[0] + " " + car_info[1], " is in the shop today at price", int(prices[last_avail]), "cr.")
        else:
            past_shop.append([car_info[0] + " " + car_info[1], last_avail, int(prices[last_avail]), "Used"])
            # print(car_info[0] + " " + car_info[1], " was last in the used shop on " + last_avail + " at price", int(prices[last_avail]), "cr.")

    if len(today_shop) > 0:
        print("\nAvailable today:")
        for car in today_shop:
            print(car[0], "is available at price", car[1], "cr. in the", car[2], "shop.")
    if len(past_shop) > 0:
        print("\nNot available today:")
        for car in past_shop:
            print(car[0], "was last available on", car[1], "at price", car[2], "cr. in the", car[3], "shop.")
    return 0

if __name__ == "__main__":
   main()