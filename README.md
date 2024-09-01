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


# Gran Turismo 7 Shops for 01-September-2024



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Ford|1932 Ford Roadster Hot Rod|400,000|
|McLaren|McLaren F1 '94|20,000,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Chevrolet|Corvette (C2) '63|239,000|
|Honda|NSX GT500 '00|1,500,000|
|Nissan|GT-R GT500 '99|2,500,000|
|Porsche|962 C '88|1,300,000|
|Toyota|Supra GT500 '97|1,800,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Chaparral|2J '70|2,500,000|
|Chevrolet|Chevelle SS 454 Sport Coupé '70|172,000|
|Ferrari|330 P4 '67|20,000,000|
|Jaguar|E-type Coupe '61|227,000|
|Porsche|917K '70|18,000,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Daihatsu|Copen '02|15,700|
|Ferrari|Testarossa '91|392,500|
|Suzuki|Swift Sport '07|11,800|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Ferrari|Dino 246 GT '71|400,000|
|Lamborghini|Murcielago LP 640 '09|318,700|
|Maserati|GranTurismo S '08|137,700|
|Mazda|Eunos Roadster (NA) '89|28,600|
|McLaren|MP4-12C '10|194,100|
|Nissan|R34 GT-R V-spec II Nur '02|401,100|
|Porsche|911 GT3 (997) '09|140,200|
|RUF|CTR3 '07|770,800|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|BMW|Z8 '01|267,200|
|Chevrolet|Corvette Convertible (C3) '69|58,200|
|Ferrari|458 Italia '09|243,200|
|Ford|Mustang Mach 1 '71|40,800|
|Honda|Civic SiR-II (EG) '93|52,500|
|Honda|Civic Type R (EK) Touring Car|122,400|
|Honda|Integra Type R (DC2) '98|62,200|
|Mitsubishi|Lancer Evolution IV GSR '96|39,600|
|Mitsubishi|Lancer Evolution V GSR '98|80,100|
|Nissan|R32 GT-R V-spec II '94|178,600|
|Nissan|Sileighty '98|81,600|
|Nissan|Skyline GTS-R (R31) '87|162,200|
|Pontiac|Firebird Trans Am '78|87,900|
|Subaru|Impreza Coupe WRX Type R STi Ver.VI '99|55,000|
|Toyota|Corolla Levin 1600GT APEX (AE86) '83|48,900|
|Toyota|Sports 800 '65|46,300|
|Volkswagen|Sambabus Typ 2 '62|67,400|
|Volvo|240 SE Estate '93|47,000|
