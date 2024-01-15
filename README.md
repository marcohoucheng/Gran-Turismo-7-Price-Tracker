# Gran Turismo 7 price tracker for used cars and legendary cars

This is a personal project built on Python and using data from https://github.com/ddm999/gt7info, it consists 3 main parts

1. A script to build a local database with the data available on the above responstory
2. An update script to run update the local database (ideally this should be automated to run once a day)
3. An email subscription service for daily updates regarding available cars in game.

A similar service is already available on https://gtdb.io. However, an account is needed to receive daily emails. The approach of this project is to provide a solution without setting an account.

# Outlook

1. Provide a method to allow creating wish lists within the mail subscription.
2. A web app to show historic prices of cars and specs.