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


# Gran Turismo 7 Shops for 10-May-2024



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Toyota|GT-One (TS020) '99|2,500,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Dodge|Charger R/T 426 Hemi '68|158,000|
|Jaguar|XJ13 '66|12,000,000|
|Lamborghini|Countach LP400 '74|1,250,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Aston Martin|DB5 '64|892,000|
|Ferrari|250 GT Berlinetta passo corto '61|8,400,000|
|Nissan|Fairlady Z 432 '69|190,000|
|Nissan|GT-R GT500 '99|2,700,000|
|Pontiac|GTO 'The Judge' '69|279,000|
|Shelby|Cobra Daytona Coupe '64|20,000,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Dodge|Super Bee '70|71,900|
|McLaren|MP4-12C '10|197,300|
|Porsche|911 Carrera RS (993) '95|215,600|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Audi|R8 4.2 '07|137,600|
|Chevrolet|Corvette ZR1 (C6) '09|98,400|
|Honda|Civic Type R (EK) '98|47,400|
|Honda|Integra Type R (DC2) '95|61,200|
|Mercedes-Benz|SLR McLaren '09|493,500|
|Volkswagen|Scirocco R '10|42,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Abarth|Abarth 595 SS '70|57,000|
|Autobianchi|A112 Abarth '85|31,800|
|BMW|M3 Sport Evolution '89|179,700|
|Ferrari|308 GTB '75|166,400|
|Ford|Sierra RS 500 Cosworth '87|193,500|
|Honda|S2000 '99|100,100|
|Honda|S800 '66|49,600|
|Lamborghini|Countach 25th Anniversary '88|711,800|
|Lancia|Delta HF Integrale Evoluzione '91|101,900|
|Lancia|Stratos '73|495,800|
|Mitsubishi|Lancer Evolution III GSR '95|87,800|
|Nissan|R33 GT-R V-spec '97|155,200|
|Nissan|Sileighty '98|72,400|
|Nissan|Silvia Q's (S13) '88|31,900|
|Pontiac|Firebird Trans Am '78|110,000|
|Renault|R5 Turbo '80|147,400|
|Suzuki|Cappuccino (EA11R) '91|17,700|
|Toyota|Sprinter Trueno 1600GT APEX (S.Shigeno Version)|97,800|
