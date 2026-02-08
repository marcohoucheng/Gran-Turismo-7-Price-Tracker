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


# Gran Turismo 7 Shops for 08-February-2026



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Porsche|917K '70|20,000,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Porsche|356 A/1500 GS Carrera '56|618,000|
|Porsche|911 GT1 Strassenversion '97|10,000,000|
|Porsche|959 '87|1,900,000|
|Porsche|962 C '88|1,250,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Chevrolet|Chevelle SS 454 Sport Coupé '70|146,000|
|Chevrolet|Corvette (C2) '63|268,000|
|Ferrari|500 Mondial Pinin Farina Coupe '54|2,000,000|
|Jaguar|E-type Coupe '61|172,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Mitsubishi|FTO GP Version R '97|26,200|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|MiTo '09|22,700|
|BMW|3.0 CSL '71|148,100|
|BMW|3.0 CSL '73|203,800|
|Lamborghini|Gallardo LP 560-4 '08|249,000|
|Nissan|R32 GT-R V-spec II '94|173,400|
|Nissan|Skyline GTS-R (R31) '87|169,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Audi|R8 4.2 '07|143,500|
|BMW|Z8 '01|265,800|
|Chevrolet|Corvette Convertible (C3) '69|47,000|
|Chevrolet|Corvette ZR1 (C6) '09|107,700|
|Citroen|BX 19 TRS '87|25,700|
|Dodge|Viper SRT10 Coupe '06|112,300|
|Ferrari|458 Italia '09|252,200|
|Fiat|Panda 30 CL '85|14,000|
|Ford|Escort RS Cosworth '92|128,900|
|Honda|NSX Type R '92|399,200|
|Lancia|Stratos '73|539,800|
|Mitsubishi|Lancer Evolution IV GSR '96|46,300|
|Mitsubishi|Lancer Evolution VI GSR T.M. SCP '99|165,200|
|Nissan|Sileighty '98|84,800|
|Peugeot|205 GTI '88|70,000|
|Porsche|911 GT3 (996) '01|154,800|
|Renault|Kangoo 1.4 '01|13,200|
|Renault|R5 Turbo '80|154,500|
|TVR|Tuscan Speed 6 '00|95,000|
|Toyota|Celica GT-Four (ST205) '94|65,500|
|Toyota|Prius G '09|21,500|
