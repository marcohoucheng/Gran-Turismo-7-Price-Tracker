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


# Gran Turismo 7 Shops for 25-May-2025



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|De Tomaso|Mangusta (Christian Dior)|500,000|
|Ferrari|365 GTB4 '71|610,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Chaparral|2J '70|2,500,000|
|Chevrolet|Chevelle SS 454 Sport Coupé '70|146,000|
|Ford|1932 Ford Roadster Hot Rod|350,000|
|Jaguar|E-type Coupe '61|205,000|
|Maserati|Merak SS '80|64,200|
|Nissan|Fairlady Z 432 '69|312,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Aston Martin|DB3S '53|6,000,000|
|Ferrari|330 P4 '67|20,000,000|
|McLaren|McLaren F1 '94|20,000,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Fiat|500 1.2 8V Lounge SS '08|13,800|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Ferrari|Testarossa '91|383,800|
|Honda|Beat '91|15,400|
|Maserati|GranTurismo S '08|146,000|
|Mazda|Eunos Roadster (NA) '89|30,600|
|Mitsubishi|Lancer Evolution V GSR '98|73,400|
|Pontiac|Firebird Trans Am '78|110,000|
|Porsche|911 Turbo (930) '81|216,500|
|Subaru|Impreza Coupe WRX Type R STi Ver.VI '99|62,700|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Abarth|Abarth 500 '09|21,700|
|BMW|M3 '97|84,200|
|BMW|Z8 '01|259,000|
|Chevrolet|Corvette Z06 (C5) '01|54,200|
|Chevrolet|Corvette ZR-1 (C4) '89|88,100|
|Chevrolet|Corvette ZR1 (C6) '09|107,700|
|Dodge|Viper SRT10 Coupe '06|112,300|
|Ferrari|Dino 246 GT '71|330,500|
|Ford|Mustang Mach 1 '71|36,200|
|Honda|Civic Type R (EK) Touring Car|114,600|
|Mazda|RX-7 GT-X (FC) '90|62,900|
|Mitsubishi|GTO Twin Turbo '91|42,300|
|Nissan|Silvia K's Aero (S14) '96|58,100|
|Porsche|911 Carrera RS CS (993) '95|436,200|
|Toyota|Corolla Levin 1600GT APEX (AE86) '83|47,400|
|Toyota|Sports 800 '65|51,400|
|Toyota|Supra 3.0GT Turbo A '88|116,800|
|Volvo|240 SE Estate '93|48,700|
