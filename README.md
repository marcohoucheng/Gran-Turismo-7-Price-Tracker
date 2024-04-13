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


# Gran Turismo 7 Shops for 13-April-2024



## Legend shop

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Chevrolet|Corvette Stingray Racer Concept '59|4,000,000|
|Lamborghini|Countach LP400 '74|1,250,000|
|Lamborghini|Miura P400 Bertone Prototype '67|3,750,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Dodge|Challenger R/T '70|233,000|
|Ford|GT40 Mark I '66|6,700,000|
|Mercedes-Benz|300 SL (W194) '52|20,000,000|
|Nissan|R92CP '92|2,000,000|
|Plymouth|Superbird '70|529,000|
|Porsche|356 A/1500 GS GT Carrera Speedster '56|1,500,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Honda|Civic Type R (EK) '97|58,100|
|Honda|NSX Type R '92|398,700|
|Mitsubishi|Lancer Evolution V GSR '98|77,500|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|BMW|Z8 '01|259,100|
|Dodge|Super Bee '70|71,900|
|Honda|S2000 '99|100,100|
|Honda|S800 '66|49,600|
|Nissan|Sileighty '98|72,400|
|Porsche|911 Carrera RS (993) '95|260,000|
|Renault|R5 Turbo '80|147,400|
|Subaru|Impreza Sedan WRX STi '04|47,100|
|Suzuki|Cappuccino (EA11R) '91|17,700|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|BMW|3.0 CSL '71|141,500|
|BMW|3.0 CSL '73|211,200|
|Ferrari|458 Italia '09|248,000|
|Ferrari|Dino 246 GT '71|343,900|
|Ferrari|Testarossa '91|372,000|
|Ford|Sierra RS 500 Cosworth '87|193,500|
|Honda|Civic Type R (EK) Touring Car|115,400|
|Lancia|Delta HF Integrale Evoluzione '91|101,900|
|Mazda|Eunos Roadster (NA) '89|26,500|
|Mitsubishi|GTO Twin Turbo '91|40,000|
|Nissan|Fairlady 240ZG (HS30) '71|98,500|
|Porsche|911 Carrera RS CS (993) '95|409,500|
|Porsche|911 Turbo (930) '81|215,600|
