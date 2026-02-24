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


# Gran Turismo 7 Shops for 24-February-2026



## Legend shop

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Abarth|1500 Biposto Bertone B.A.T 1 '52|1,000,000|
|Mercedes-Benz|CLK-LM '98|8,500,000|
|Nissan|Skyline 2000GT-R (KPGC110) '73|537,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|8C 2900B Touring Berlinetta '38|20,000,000|
|Chevrolet|Corvette (C1) '58|122,000|
|Ford|Mustang Boss 429 '69|349,000|
|Jaguar|XJ13 '66|12,000,000|
|Jaguar|XJR-9 '88|3,000,000|
|Peugeot|205 Turbo 16 Evolution 2 '86|1,000,000|
|Toyota|Celica GT-FOUR Rally Car (ST205) '95|210,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Pontiac|Firebird Trans Am '78|84,500|
|Volkswagen|Scirocco R '10|38,600|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Fiat|500 1.2 8V Lounge SS '08|12,700|
|Honda|Civic Type R (EK) '97|47,000|
|Nissan|Fairlady Z 300ZX TT 2seater '89|58,000|
|Renault|Clio V6 24V '00|73,600|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alpine|A110 '72|134,500|
|Autobianchi|A112 Abarth '85|32,000|
|BMW|M3 '03|67,800|
|BMW|M3 '07|72,500|
|BMW|M3 '89|73,100|
|Chevrolet|Corvette Stingray (C3) '69|62,000|
|Daihatsu|Copen '02|16,100|
|Dodge|Viper GTS '02|104,900|
|Ferrari|430 Scuderia '07|363,800|
|Ferrari|F430 '06|202,200|
|Ford|Sierra RS 500 Cosworth '87|183,500|
|MINI|Mini-Cooper 'S' '65|43,600|
|Nissan|GT-R NISMO (R32) '90|387,200|
|Nissan|SILVIA spec-R Aero (S15) '02|59,800|
|Porsche|911 Carrera RS (964) '92|225,000|
|Subaru|Impreza 22B-STi '98|164,100|
|Suzuki|Swift Sport '07|12,100|
|Toyota|Sports 800 '65|45,900|
