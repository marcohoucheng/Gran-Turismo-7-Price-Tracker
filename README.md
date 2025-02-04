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


# Gran Turismo 7 Shops for 04-February-2025



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Maserati|A6GCS/53 Spyder '54|3,000,000|
|Plymouth|Superbird '70|402,000|
|Plymouth|Superbird '70|402,000|
|Plymouth|Superbird '70|402,000|
|Plymouth|Superbird '70|402,000|
|Plymouth|Superbird '70|402,000|
|Toyota|Supra GT500 '97|1,800,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Toyota|GT-One (TS020) '99|2,500,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Maserati|Merak SS '80|64,200|
|Mazda|787B '91|3,300,000|
|McLaren|MP4/4 '88|12,000,000|
|Mercedes-Benz|Sauber Mercedes C9 '89|3,500,000|
|Mercedes-Benz|W 196 R '55|20,000,000|
|Nissan|Skyline Super Silhouette Group 5 '84|1,150,000|
|Porsche|962 C '88|1,300,000|
|Porsche|Carrera GTS (904) '64|2,300,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Nissan|Fairlady Z (Z34) '08|33,000|
|Pontiac|Firebird Trans Am '78|110,000|
|Pontiac|Firebird Trans Am '78|110,000|
|Pontiac|Firebird Trans Am '78|110,000|
|Pontiac|Firebird Trans Am '78|110,000|
|Pontiac|Firebird Trans Am '78|110,000|
|Renault|Clio V6 24V '00|89,700|
|Toyota|Sports 800 '65|51,400|
|Volvo|240 SE Estate '93|48,700|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|BMW|3.0 CSL '73|209,100|
|Chevrolet|Corvette ZR-1 (C4) '89|90,600|
|Ferrari|Dino 246 GT '71|333,900|
|Lamborghini|Gallardo LP 560-4 '08|249,200|
|Mazda|RX-7 GT-X (FC) '90|58,900|
|Mitsubishi|Lancer Evolution VI GSR T.M. SCP '99|162,400|
|Nissan|Silvia K's Dia Selection (S13) '90|52,100|
|Porsche|911 Carrera RS CS (993) '95|438,500|
|Renault|R4 GTL '85|24,700|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Abarth|Abarth 500 '09|21,700|
|DMC|DeLorean S2 '04|471,500|
|Ford|Escort RS Cosworth '92|129,700|
|Honda|Beat '91|15,900|
|Honda|Civic Si Extra (EF) '87|61,600|
|Lamborghini|Murcielago LP 640 '09|340,400|
|MINI|MINI Cooper S '05|23,200|
|Mazda|Eunos Roadster (NA) '89|30,600|
|Mitsubishi|Lancer Evolution VIII MR GSR '04|66,000|
|Nissan|180SX Type X '96|46,900|
|Porsche|911 GT3 (997) '09|137,000|
|Toyota|Celica GT-Four (ST205) '94|73,400|
|Toyota|Corolla Levin 1600GT APEX (AE86) '83|47,400|
|Volkswagen|Sambabus Typ 2 '62|63,500|
