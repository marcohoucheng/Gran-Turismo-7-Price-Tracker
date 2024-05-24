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


# Gran Turismo 7 Shops for 24-May-2024



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Porsche|959 '87|1,750,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Plymouth|Superbird '70|529,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Ferrari|F40 '92|3,100,000|
|Ferrari|F50 '95|4,450,000|
|Ford|Mark IV Race Car '67|6,750,000|
|Jaguar|XJ220 '92|615,000|
|Maserati|A6GCS/53 Spyder '54|2,500,000|
|Mazda|RX500 '70|600,000|
|McLaren|McLaren F1 '94|20,000,000|
|Plymouth|XNR Ghia Roadster '60|1,600,000|
|Porsche|356 A/1500 GS Carrera '56|615,000|
|Porsche|911 GT1 Strassenversion '97|10,000,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Nissan|Fairlady Z (Z34) '08|36,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Abarth|Abarth 500 '09|22,100|
|Honda|Beat '91|16,800|
|Honda|Civic Type R (EK) Touring Car|115,400|
|Mazda|Eunos Roadster (NA) '89|26,500|
|Mitsubishi|Lancer Evolution IV GSR '96|44,200|
|Mitsubishi|Lancer Evolution V GSR '98|77,500|
|Subaru|Impreza Coupe WRX Type R STi Ver.VI '99|53,600|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Chevrolet|Corvette Convertible (C3) '69|50,900|
|Dodge|Viper GTS '02|105,600|
|Dodge|Viper SRT10 Coupe '06|115,000|
|Ferrari|458 Italia '09|248,000|
|Ferrari|Dino 246 GT '71|400,000|
|Ferrari|Testarossa '91|372,000|
|Ford|Mustang Mach 1 '71|36,800|
|Honda|Integra Type R (DC2) '98|62,100|
|Honda|NSX Type R '92|398,700|
|Mitsubishi|Lancer Evolution IX MR GSR '06|99,700|
|Nissan|R32 GT-R V-spec II '94|176,500|
|Porsche|911 Carrera RS CS (993) '95|409,500|
|Porsche|911 GT3 (996) '01|155,500|
|Renault|R4 GTL '85|24,100|
|Toyota|Corolla Levin 1600GT APEX (AE86) '83|46,800|
|Toyota|Sports 800 '65|48,100|
|Toyota|Supra 3.0GT Turbo A '88|115,900|
|Volkswagen|Sambabus Typ 2 '62|57,100|
|Volkswagen|Volkswagen 1200 '66|35,800|
