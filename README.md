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


# Gran Turismo 7 Shops for 08-November-2024



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Toyota|Supra GT500 '97|1,800,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Ferrari|250 GT Berlinetta passo corto '61|8,100,000|
|Nissan|Fairlady Z 432 '69|312,000|
|Shelby|Cobra Daytona Coupe '64|20,000,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Aston Martin|DB5 '64|892,000|
|Ford|Mustang Boss 429 '69|346,000|
|Maserati|Merak SS '80|64,200|
|McLaren|MP4/4 '88|12,000,000|
|Nissan|Skyline Super Silhouette Group 5 '84|1,150,000|
|Porsche|Carrera GTS (904) '64|2,300,000|
|Toyota|GT-One (TS020) '99|2,500,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Audi|R8 4.2 '07|137,100|
|Honda|Civic Type R (EK) Touring Car|114,800|
|Honda|Integra Type R (DC2) '98|61,200|
|Volkswagen|Golf I GTI '83|40,500|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|BMW|Z8 '01|259,600|
|Daihatsu|Copen '02|16,000|
|Ferrari|Testarossa '91|367,000|
|Honda|Beat '91|20,000|
|Maserati|GranTurismo S '08|141,800|
|Mitsubishi|Lancer Evolution V GSR '98|80,700|
|Nissan|R34 GT-R V-spec II Nur '02|396,400|
|Nissan|Silvia K's Aero (S14) '96|57,800|
|RUF|CTR3 '07|771,300|
|Suzuki|Cappuccino (EA11R) '91|20,000|
|Toyota|Corolla Levin 1600GT APEX (AE86) '83|58,400|
|Volvo|240 SE Estate '93|41,800|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|BMW|M3 '97|83,000|
|Chevrolet|Corvette ZR1 (C6) '09|99,000|
|Dodge|Super Bee '70|80,000|
|Dodge|Viper SRT10 Coupe '06|111,800|
|Ferrari|458 Italia '09|242,500|
|Fiat|500 1.2 8V Lounge SS '08|14,400|
|Honda|Civic Type R (EK) '97|50,200|
|Mazda|Eunos Roadster (NA) '89|35,000|
|Mitsubishi|GTO Twin Turbo '91|41,600|
|Mitsubishi|Lancer Evolution IV GSR '96|39,600|
|Nissan|R32 GT-R V-spec II '94|178,600|
|Pontiac|Firebird Trans Am '78|87,900|
|Subaru|Impreza Coupe WRX Type R STi Ver.VI '99|62,300|
|Subaru|Impreza Sedan WRX STi '04|43,600|
|Suzuki|Swift Sport '07|11,800|
|Toyota|Sports 800 '65|47,200|
|Toyota|Supra 3.0GT Turbo A '88|112,000|
