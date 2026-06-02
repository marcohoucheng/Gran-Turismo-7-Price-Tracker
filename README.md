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


# Gran Turismo 7 Shops for 02-June-2026



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Toyota|Land Cruiser FJ40V '74|50,900|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|BMW|McLaren F1 GTR Race Car '97|20,000,000|
|Ferrari|250 GTO '62|20,000,000|
|Jaguar|XJ13 '66|12,000,000|
|Suzuki|V6 Escudo Pikes Peak Special spec.98|1,700,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|AMG|300 SEL 6.8 AMG '71|700,000|
|Dodge|Challenger R/T '70|168,000|
|Ferrari|F40 '92|3,400,000|
|Toyota|2000GT '67|982,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Porsche|911 Turbo (930) '81|213,800|
|Subaru|Impreza Coupe WRX Type R STi Ver.VI '99|62,700|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Chevrolet|Corvette ZR1 (C6) '09|101,000|
|Fiat|500 F '68|15,100|
|Mitsubishi|Lancer Evolution IX MR GSR '06|95,800|
|Porsche|911 Carrera RS (993) '95|215,200|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|AMG|SLS AMG '10|319,400|
|Abarth|Abarth 595 SS '70|49,500|
|Alfa Romeo|MiTo '09|20,600|
|BMW|3.0 CSL '71|146,100|
|BMW|M3 '97|89,000|
|Chevrolet|Corvette Z06 (C5) '01|56,200|
|Ferrari|Dino 246 GT '71|346,000|
|Fiat|Panda 30 CL '85|11,300|
|Ford|Mustang Mach 1 '71|43,600|
|Honda|Civic SiR-II (EG) '93|50,100|
|Honda|Civic Type R (EK) Touring Car|123,400|
|Lamborghini|Countach 25th Anniversary '88|659,700|
|Mazda|RX-7 GT-X (FC) '90|57,100|
|Mitsubishi|GTO Twin Turbo '91|39,600|
|Nissan|Fairlady 240ZG (HS30) '71|98,500|
|Nissan|Silvia K's Aero (S14) '96|57,600|
|Nissan|Silvia K's Dia Selection (S13) '90|52,100|
|Porsche|911 Carrera RS CS (993) '95|406,400|
|Renault|Avantime 3.0 V6 24V '02|44,900|
|Toyota|Sprinter Trueno 1600GT APEX (S.Shigeno Version)|105,800|
|Volkswagen|Volkswagen 1200 '66|32,700|
