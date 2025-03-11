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


# Gran Turismo 7 Shops for 11-March-2025



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Porsche|Spyder type 550/1500RS '55|4,850,000|
|Toyota|2000GT '67|992,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Ford|Mustang Boss 429 '69|319,000|
|Peugeot|205 Turbo 16 Evolution 2 '86|1,000,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|BMW|McLaren F1 GTR Race Car '97|20,000,000|
|Chevrolet|Corvette (C1) '58|119,000|
|Ferrari|250 GTO '62|20,000,000|
|Jaguar|XJ13 '66|12,000,000|
|Mercedes-Benz|Unimog Type 411 '62|46,000|
|Suzuki|V6 Escudo Pikes Peak Special spec.98|1,700,000|
|Toyota|Celica GT-FOUR Rally Car (ST205) '95|250,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Fiat|500 1.2 8V Lounge SS '08|13,500|
|Nissan|180SX Type X '96|55,100|
|Porsche|911 GT3 (997) '09|142,600|
|Porsche|911 Turbo (930) '81|250,000|
|Porsche|911 Turbo (930) '81|250,000|
|Toyota|Celica GT-Four (ST205) '94|80,900|
|Toyota|Sports 800 '65|47,400|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|BMW|3.0 CSL '73|204,700|
|Chevrolet|Corvette ZR1 (C6) '09|98,200|
|Dodge|Viper SRT10 Coupe '06|113,900|
|Honda|Beat '91|17,500|
|Honda|Civic Si Extra (EF) '87|59,900|
|Honda|Civic Type R (EK) Touring Car|123,400|
|Mitsubishi|Lancer Evolution VI GSR T.M. SCP '99|166,900|
|Nissan|Skyline GTS-R (R31) '87|171,600|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Abarth|Abarth 500 '09|23,500|
|Audi|R8 4.2 '07|145,400|
|BMW|Z4 3.0i '03|44,600|
|Ferrari|458 Italia '09|250,400|
|Ford|Escort RS Cosworth '92|123,900|
|Honda|NSX Type R '92|404,400|
|Lamborghini|Gallardo LP 560-4 '08|239,100|
|Lancia|Stratos '73|522,600|
|Mazda|Eunos Roadster (NA) '89|28,600|
|Mitsubishi|Lancer Evolution VIII MR GSR '04|65,900|
|Nissan|Sileighty '98|72,400|
|Peugeot|205 GTI '88|61,600|
|Porsche|911 GT3 (996) '01|158,400|
|Toyota|Corolla Levin 1600GT APEX (AE86) '83|51,900|
|Volkswagen|Sambabus Typ 2 '62|54,700|
|Volvo|240 SE Estate '93|41,200|
