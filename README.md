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


# Gran Turismo 7 Shops for 13-November-2024



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Ferrari|F50 '95|4,450,000|
|Mazda|RX500 '70|600,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Nissan|Skyline Super Silhouette Group 5 '84|1,150,000|
|Porsche|Carrera GTS (904) '64|2,300,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Jaguar|XJ220 '92|615,000|
|Maserati|A6GCS/53 Spyder '54|2,500,000|
|Maserati|Merak SS '80|64,200|
|Porsche|356 A/1500 GS Carrera '56|618,000|
|Toyota|Supra GT500 '97|1,800,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|MiTo '09|22,700|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|BMW|M3 '97|83,000|
|Chevrolet|Corvette ZR1 (C6) '09|99,000|
|Dodge|Viper SRT10 Coupe '06|111,800|
|Honda|Civic Type R (EK) Touring Car|114,800|
|Mitsubishi|GTO Twin Turbo '91|41,600|
|Subaru|Impreza Coupe WRX Type R STi Ver.VI '99|62,300|
|Subaru|Impreza Sedan WRX STi '04|43,600|
|Volkswagen|Golf I GTI '83|40,500|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alpine|A110 '72|142,200|
|Audi|R8 4.2 '07|137,100|
|Chevrolet|Corvette Convertible (C3) '69|53,000|
|Chevrolet|Corvette ZR-1 (C4) '89|90,600|
|Ford|Mustang Mach 1 '71|36,100|
|Honda|Integra Type R (DC2) '98|61,200|
|Honda|NSX Type R '92|402,700|
|Lamborghini|Gallardo LP 560-4 '08|249,200|
|MINI|Mini-Cooper 'S' '65|40,800|
|Mazda|Eunos Roadster (NA) '89|35,000|
|Mitsubishi|Lancer Evolution IV GSR '96|39,600|
|Nissan|R32 GT-R V-spec II '94|178,600|
|Nissan|Silvia K's Type S (S14) '94|51,400|
|Nissan|Skyline GTS-R (R31) '87|179,600|
|Porsche|911 Carrera RS CS (993) '95|438,500|
|Porsche|911 GT3 (996) '01|155,600|
|Porsche|911 GT3 (997) '09|137,000|
|Suzuki|Swift Sport '07|11,800|
|Toyota|Sprinter Trueno 1600GT APEX (AE86) '83|51,900|
