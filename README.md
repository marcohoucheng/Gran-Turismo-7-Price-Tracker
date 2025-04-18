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


# Gran Turismo 7 Shops for 18-April-2025



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Mercedes-Benz|300 SL Coupe '54|1,700,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Mercedes-Benz|190 E 2.5-16 Evolution II '91|290,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Honda|NSX GT500 '00|1,500,000|
|Maserati|A6GCS/53 Spyder '54|3,000,000|
|Mercedes-Benz|S Barker Tourer '29|13,000,000|
|Porsche|Spyder type 550/1500RS '55|4,850,000|


## Used shop

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Ferrari|Dino 246 GT '71|352,300|
|Ford|Mustang Mach 1 '71|37,500|
|Honda|Beat '91|15,900|
|Honda|Civic SiR-II (EG) '93|60,000|
|Honda|Civic Type R (EK) '97|65,000|
|Honda|Civic Type R (EK) '98|65,000|
|Mitsubishi|GTO Twin Turbo '91|45,000|
|Volkswagen|Sambabus Typ 2 '62|55,600|
|Volvo|240 SE Estate '93|46,600|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Abarth|Abarth 500 '09|26,400|
|Audi|R8 4.2 '07|144,600|
|Chevrolet|Corvette Convertible (C3) '69|53,800|
|Chevrolet|Corvette Stingray (C3) '69|71,500|
|Chevrolet|Corvette Stingray (C3) '69|71,500|
|Chevrolet|Corvette ZR1 (C6) '09|107,400|
|Dodge|Super Bee '70|70,600|
|Dodge|Viper SRT10 Coupe '06|114,000|
|Ferrari|458 Italia '09|243,100|
|Fiat|500 1.2 8V Lounge SS '08|12,700|
|Honda|Civic Type R (EK) Touring Car|117,000|
|Honda|NSX Type R '92|385,600|
|Lamborghini|Gallardo LP 560-4 '08|253,400|
|Mitsubishi|Lancer Evolution IV GSR '96|44,200|
|Nissan|R32 GT-R V-spec II '94|176,500|
|Nissan|Skyline GTS-R (R31) '87|166,500|
|Peugeot|205 GTI '88|70,000|
|Peugeot|205 GTI '88|70,000|
|Peugeot|205 GTI '88|70,000|
|Porsche|911 GT3 (996) '01|158,500|
|Toyota|Corolla Levin 1600GT APEX (AE86) '83|51,200|
|Toyota|Sports 800 '65|45,900|
