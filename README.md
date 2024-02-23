# Gran Turismo 7 price tracker for used cars and legendary cars

This is a personal project built on Python and using data from https://github.com/ddm999/gt7info, it consists 3 main parts

1. A script to build a local database with the data available on the above responstory
2. An update script to run update the local database (ideally this should be automated to run once a day)
3. An email subscription service for daily updates regarding available cars in game.

A similar service is already available on https://gtdb.io. However, an account is needed to receive daily emails. The approach of this project is to provide a solution without setting an account.

# Outlook

1. Create a more seamless solution to build and run script.
2. Provide a method to return cars avaialbe of the day.
3. Provide a method to allow creating wish lists within the mail subscription.
4. A web app to show historic prices of cars and specs.

# How to use

1. Build databases by running `build.py`, `shop.py` and `car.py`.
2. Run `update.py` before running `wish.py` when checking whather cars on wish list are available.