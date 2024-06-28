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


# Gran Turismo 7 Shops for 28-June-2024



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Ford|Mark IV Race Car '67|6,750,000|
|Renault|R8 Gordini '66|32,500|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Chevrolet|Corvette (C1) '58|119,000|
|Suzuki|V6 Escudo Pikes Peak Special spec.98|1,700,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|AMG|300 SEL 6.8 AMG '71|700,000|
|Ferrari|F40 '92|3,100,000|
|Jaguar|XJR-9 '88|3,000,000|
|Nissan|Skyline Hard Top 2000GT-R (KPGC10) '70|194,000|
|Pontiac|GTO 'The Judge' '69|268,000|
|Porsche|356 A/1500 GS Carrera '56|618,000|
|Porsche|356 A/1500 GS GT Carrera Speedster '56|1,600,000|
|Toyota|2000GT '67|992,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Nissan|Silvia K's Type S (S14) '94|53,900|
|Toyota|Celica GT-Four (ST205) '94|80,700|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Ford|Mustang Mach 1 '71|36,800|
|Honda|Integra Type R (DC2) '98|62,100|
|Lamborghini|Murcielago LP 640 '09|337,200|
|Maserati|GranTurismo S '08|147,400|
|McLaren|MP4-12C '10|197,300|
|Nissan|R32 GT-R V-spec II '94|176,500|
|Nissan|R34 GT-R V-spec II Nur '02|396,600|
|Porsche|911 GT3 (997) '09|142,500|
|RUF|CTR3 '07|801,800|
|Toyota|Supra 3.0GT Turbo A '88|115,900|
|Volkswagen|Sambabus Typ 2 '62|57,100|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alpine|A110 '72|137,500|
|BMW|Z8 '01|259,100|
|Chevrolet|Corvette Convertible (C3) '69|50,900|
|Daihatsu|Copen '02|13,000|
|Ferrari|458 Italia '09|248,000|
|Honda|Civic Type R (EK) Touring Car|115,400|
|Mazda|RX-7 GT-X (FC) '90|61,100|
|Mitsubishi|Lancer Evolution III GSR '95|100,000|
|Mitsubishi|Lancer Evolution VI GSR T.M. SCP '99|168,100|
|Pontiac|Firebird Trans Am '78|81,700|
|Suzuki|Swift Sport '07|12,200|
|Toyota|Corolla Levin 1600GT APEX (AE86) '83|46,800|
|Toyota|Sports 800 '65|48,100|
|Volkswagen|Golf I GTI '83|46,700|
