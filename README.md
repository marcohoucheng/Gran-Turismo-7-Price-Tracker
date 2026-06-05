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


# Gran Turismo 7 Shops for 05-June-2026



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Ford|Mark IV Race Car '67|6,750,000|
|Nissan|R92CP '92|2,000,000|
|Renault|R8 Gordini '66|32,500|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Toyota|2000GT '67|982,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Chevrolet|Corvette Stingray Racer Concept '59|7,000,000|
|Dodge|Challenger R/T '70|168,000|
|Ferrari|F40 '92|3,400,000|
|Subaru|Impreza Rally Car '98|650,000|
|Toyota|Land Cruiser FJ40V '74|50,900|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|BMW|3.0 CSL '73|206,600|
|Nissan|R34 GT-R V-spec II Nur '02|398,700|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Lamborghini|Countach 25th Anniversary '88|659,700|
|Nissan|Silvia K's Dia Selection (S13) '90|52,100|
|Porsche|911 Carrera RS CS (993) '95|406,400|
|Renault|Avantime 3.0 V6 24V '02|44,900|
|Volkswagen|Volkswagen 1200 '66|32,700|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|AMG|SLS AMG '10|319,400|
|Alfa Romeo|MiTo '09|20,600|
|BMW|3.0 CSL '71|146,100|
|BMW|M3 '97|89,000|
|Chevrolet|Corvette Z06 (C5) '01|56,200|
|Ferrari|Dino 246 GT '71|346,000|
|Ferrari|Testarossa '91|368,500|
|Fiat|Panda 30 CL '85|11,300|
|Ford|Mustang Mach 1 '71|43,600|
|Honda|Civic Type R (EK) Touring Car|123,400|
|Lamborghini|Diablo GT '00|785,300|
|Mazda|RX-7 GT-X (FC) '90|57,100|
|Mitsubishi|GTO Twin Turbo '91|39,600|
|Mitsubishi|Lancer Evolution V GSR '98|73,400|
|Nissan|Silvia K's Aero (S14) '96|57,600|
|Porsche|911 Turbo (930) '81|213,800|
|RUF|CTR3 '07|788,800|
|Subaru|Impreza Coupe WRX Type R STi Ver.VI '99|62,700|
|Toyota|Supra 3.0GT Turbo A '88|116,800|
