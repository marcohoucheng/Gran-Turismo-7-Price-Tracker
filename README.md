# Gran Turismo 7 tracker for in-game dynamic prices for cars

This is a personal project built on Python to obtain in-game stores information of Gran Turismo 7 without the necessarity to manually start the game on PlayStation 5. It has the following functionalities:

- An automated daily email to list updates in game.
- Aggregate data to build a local database of cars' historical prices,
- Return latest information of cars given a wish list.

Data are scraped from https://github.com/ddm999/gt7info. Tools providing similar information are available on https://gtdb.io. However, the site requires an account to receive daily emails. The setup of this project allows for a setup without having to sign up for an account.

The approach of this project is to provide a solution without setting an account.

# Usage

## Daily Email

A scheduled Github Action is currently set up. However, the user can easily set up a similar system. Only `email_update.py` is needed in this case with the appropriate environment varibles for `SENDER_EMAIL`, `PASSWORD` and `RECIPIENTS`. A [screenshot](https://raw.githubusercontent.com/marcohoucheng/Gran-Turismo-7-Price-Tracker/main/data/email_screenshot.png) of the email and the latest html copy is shown below.

## Wish list and local database

1. Build databases by running `build.py`. It will also detect whether `shop.py` and `car.py` should be run.
    - Only the respective shop will be built if ran with flag `used` or `legend`. Nevertheless, `shop.py` and `car.py` will still be triggered if necessary.
2. Run `update.py` to update the local shop databases.
    - Similar to `build.py`, `used` or `legend` flags can be called.
3. `wish.py` checks whether cars in the wish list `wish_list.txt` are available today. If so, then it will return the price. Otherwise, it returns the last available date and the price.
    - This script will automatically run `update.py` when checking whather cars on wish list are available.
4. Running `today.py` returns items available in the shops in terminal. With flag `new` the script will only return new days of the day.


# Gran Turismo 7 Shops for 09-March-2025



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Ferrari|250 GTO '62|20,000,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Abarth|1500 Biposto Bertone B.A.T 1 '52|1,000,000|
|Alfa Romeo|8C 2900B Touring Berlinetta '38|20,000,000|
|Mercedes-Benz|300 SL Coupe '54|1,700,000|
|Mercedes-Benz|300 SL Coupe '54|1,700,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|BMW|McLaren F1 GTR Race Car '97|20,000,000|
|Ford|Mustang Boss 429 '69|319,000|
|Jaguar|XJ13 '66|12,000,000|
|Mercedes-Benz|Unimog Type 411 '62|46,000|
|Peugeot|205 Turbo 16 Evolution 2 '86|1,000,000|
|Suzuki|V6 Escudo Pikes Peak Special spec.98|1,700,000|
|Toyota|Celica GT-FOUR Rally Car (ST205) '95|250,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Abarth|Abarth 500 '09|23,500|
|Ford|Escort RS Cosworth '92|123,900|
|Toyota|Corolla Levin 1600GT APEX (AE86) '83|51,900|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Chevrolet|Corvette Convertible (C3) '69|51,300|
|Chevrolet|Corvette ZR-1 (C4) '89|79,100|
|Dodge|Super Bee '70|71,700|
|Ferrari|Dino 246 GT '71|343,200|
|Mitsubishi|Lancer Evolution IV GSR '96|42,000|
|Nissan|R32 GT-R V-spec II '94|179,800|
|Nissan|Silvia Q's (S13) '88|33,900|
|Peugeot|205 GTI '88|62,700|
|Peugeot|205 GTI '88|60,100|
|Renault|R4 GTL '85|29,100|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Audi|R8 4.2 '07|145,400|
|BMW|3.0 CSL '73|204,700|
|BMW|Z4 3.0i '03|44,600|
|Chevrolet|Corvette ZR1 (C6) '09|98,200|
|Dodge|Viper SRT10 Coupe '06|113,900|
|Ferrari|458 Italia '09|250,400|
|Honda|Beat '91|17,500|
|Honda|Civic Si Extra (EF) '87|59,900|
|Honda|Civic Type R (EK) Touring Car|123,400|
|Lamborghini|Gallardo LP 560-4 '08|239,100|
|Lancia|Stratos '73|522,600|
|Mazda|Eunos Roadster (NA) '89|28,600|
|Mitsubishi|Lancer Evolution VI GSR T.M. SCP '99|166,900|
|Nissan|Sileighty '98|72,400|
|Nissan|Skyline GTS-R (R31) '87|171,600|
|Peugeot|205 GTI '88|61,600|
|Volkswagen|Sambabus Typ 2 '62|54,700|
