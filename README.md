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


# Gran Turismo 7 Shops for 01-March-2026



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Toyota|2000GT '67|982,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Chevrolet|Corvette (C1) '58|122,000|
|Ford|Mustang Boss 429 '69|349,000|
|Jaguar|XJR-9 '88|3,000,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|BMW|McLaren F1 GTR Race Car '97|20,000,000|
|Ferrari|250 GTO '62|20,000,000|
|Jaguar|XJ13 '66|12,000,000|
|Suzuki|V6 Escudo Pikes Peak Special spec.98|1,700,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Honda|Integra Type R (DC2) '98|65,900|
|Toyota|Sprinter Trueno 1600GT APEX (AE86) '83|52,100|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alpine|A110 '72|134,500|
|BMW|M3 '03|67,800|
|BMW|M3 '89|73,100|
|Nissan|GT-R NISMO (R32) '90|387,200|
|Pontiac|Firebird Trans Am '78|84,500|
|Subaru|Impreza 22B-STi '98|164,100|
|Suzuki|Swift Sport '07|12,100|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Autobianchi|A112 Abarth '85|32,000|
|BMW|M3 Sport Evolution '89|162,800|
|Ford|Sierra RS 500 Cosworth '87|183,500|
|Honda|Civic Type R (EK) '98|53,500|
|Honda|S2000 '99|98,700|
|Mazda|RX-7 Spirit R Type A (FD) '02|219,900|
|Mercedes-Benz|SLR McLaren '09|509,900|
|Mitsubishi|Lancer Evolution III GSR '95|84,600|
|Nissan|R33 GT-R V-spec '97|160,500|
|Nissan|Silvia K's Type S (S14) '94|43,200|
|Subaru|Impreza Sedan WRX STi '04|41,100|
|Suzuki|Cappuccino (EA11R) '91|16,900|
|TVR|Tuscan Speed 6 '00|73,200|
|Volkswagen|Golf I GTI '83|43,200|
|Volkswagen|Scirocco R '10|38,600|
