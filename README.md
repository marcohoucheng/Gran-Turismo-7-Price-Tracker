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


# Gran Turismo 7 Shops for 21-June-2024



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Chevrolet|Corvette (C1) '58|119,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Ferrari|F40 '92|3,100,000|
|Ferrari|F50 '95|4,450,000|
|Peugeot|205 Turbo 16 Evolution 2 '86|1,100,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Aston Martin|DB5 '64|892,000|
|BMW|McLaren F1 GTR Race Car '97|20,000,000|
|Ferrari|250 GTO '62|20,000,000|
|Ford|Mustang Boss 429 '69|346,000|
|Jaguar|XJ13 '66|12,000,000|
|Suzuki|V6 Escudo Pikes Peak Special spec.98|1,700,000|
|Toyota|Celica GT-FOUR Rally Car (ST205) '95|250,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|AMG|SLS AMG '10|308,300|
|BMW|Z8 '01|259,100|
|Maserati|GranTurismo S '08|147,400|
|Mitsubishi|Lancer Evolution IV GSR '96|44,200|
|Nissan|R32 GT-R V-spec II '94|176,500|
|Renault|R4 GTL '85|24,100|
|Subaru|Impreza Coupe WRX Type R STi Ver.VI '99|53,600|
|Toyota|Supra 3.0GT Turbo A '88|115,900|
|Volkswagen|Sambabus Typ 2 '62|57,100|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|BMW|3.0 CSL '73|211,200|
|Honda|Civic Type R (EK) '97|58,100|
|Lamborghini|Countach 25th Anniversary '88|711,800|
|Mitsubishi|GTO Twin Turbo '91|40,000|
|Nissan|R33 GT-R V-spec '97|155,200|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Abarth|Abarth 500 '09|22,100|
|Fiat|500 1.2 8V Lounge SS '08|13,300|
|Honda|Beat '91|16,800|
|Honda|Civic SiR-II (EG) '93|52,100|
|Mazda|Eunos Roadster (NA) '89|26,500|
|McLaren|MP4-12C '10|197,300|
|Mitsubishi|Lancer Evolution V GSR '98|77,500|
|Nissan|R34 GT-R V-spec II Nur '02|396,600|
|Nissan|Silvia K's Aero (S14) '96|59,300|
|Nissan|Silvia K's Dia Selection (S13) '90|49,700|
|Nissan|Skyline GTS-R (R31) '87|176,600|
|Porsche|911 Carrera RS (993) '95|215,600|
|Porsche|911 Turbo (930) '81|215,600|
|RUF|CTR3 '07|801,800|
|TVR|Tuscan Speed 6 '00|95,000|
|Volkswagen|Volkswagen 1200 '66|35,800|
|Volvo|240 SE Estate '93|40,800|
