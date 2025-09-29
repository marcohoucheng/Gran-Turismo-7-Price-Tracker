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


# Gran Turismo 7 Shops for 29-September-2025



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Audi|Sport quattro S1 Pikes Peak '87|1,800,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alpine|A220 Race Car '68|330,000|
|Ferrari|330 P4 '67|20,000,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Citroen|DS 21 Pallas '70|49,500|
|Dodge|Challenger R/T '70|179,000|
|Jeep|Willys MB '45|31,300|
|Porsche|911 Carrera RS (901) '73|740,000|
|Shelby|G.T.350 '65|455,000|
|Toyota|Land Cruiser FJ40V '74|44,100|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Ferrari|458 Italia '09|244,400|
|Honda|NSX Type R '92|398,200|
|Mitsubishi|Lancer Evolution IV GSR '96|46,300|
|Nissan|R32 GT-R V-spec II '94|173,400|
|Suzuki|Cappuccino (EA11R) '91|16,200|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alpine|A110 '72|143,800|
|Autobianchi|A112 Abarth '85|29,100|
|BMW|M3 '97|80,400|
|Ferrari|Dino 246 GT '71|327,300|
|Ford|Mustang Mach 1 '71|41,400|
|Honda|Civic Type R (EK) Touring Car|122,800|
|Porsche|911 Carrera RS CS (993) '95|409,200|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Audi|R8 4.2 '07|136,500|
|Chevrolet|Corvette ZR-1 (C4) '89|84,600|
|Chevrolet|Corvette ZR1 (C6) '09|99,200|
|Citroen|BX 19 TRS '87|30,000|
|Dodge|Super Bee '70|61,100|
|Dodge|Viper SRT10 Coupe '06|115,300|
|Lamborghini|Gallardo LP 560-4 '08|252,000|
|Lancia|Delta HF Integrale Evoluzione '91|101,200|
|Mazda|RX-7 GT-X (FC) '90|62,800|
|Nissan|SILVIA spec-R Aero (S15) '02|68,000|
|Nissan|Silvia K's Dia Selection (S13) '90|56,800|
|Nissan|Silvia K's Type S (S14) '94|50,800|
|Nissan|Skyline GTS-R (R31) '87|169,000|
|Peugeot|205 GTI '88|54,100|
|Renault|Avantime 3.0 V6 24V '02|37,600|
|Volkswagen|Volkswagen 1200 '66|31,900|
