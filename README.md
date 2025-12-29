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


# Gran Turismo 7 Shops for 29-December-2025



## Legend shop

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|NISMO|400R '95|1,600,000|
|Porsche|911 Carrera RS (901) '73|740,000|
|Shelby|G.T.350 '65|491,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Audi|Sport quattro S1 Pikes Peak '87|1,800,000|
|Citroen|DS 21 Pallas '70|49,500|
|Jeep|Willys MB '45|31,300|
|Nissan|Skyline Hard Top 2000GT-R (KPGC10) '70|194,000|
|Shelby|Cobra 427 '66|2,700,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Audi|TT Coupe 3.2 quattro '03|43,300|
|Lamborghini|Murcielago LP 640 '09|340,400|
|Nissan|Silvia Q's (S13) '88|31,500|
|Porsche|911 GT3 (997) '09|140,900|
|Toyota|Celica GT-Four (ST205) '94|65,500|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Abarth|Abarth 595 SS '70|53,100|
|Alfa Romeo|MiTo '09|22,700|
|BMW|3.0 CSL '71|141,800|
|BMW|3.0 CSL '73|205,200|
|Fiat|500 F '68|17,900|
|Mitsubishi|Lancer Evolution IV GSR '96|46,300|
|Nissan|R32 GT-R V-spec II '94|173,400|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Audi|R8 4.2 '07|136,500|
|Chevrolet|Corvette Convertible (C3) '69|47,000|
|Citroen|BX 19 TRS '87|22,700|
|Ferrari|458 Italia '09|244,400|
|Ford|Escort RS Cosworth '92|128,900|
|Honda|NSX Type R '92|398,200|
|Lamborghini|Gallardo LP 560-4 '08|252,000|
|Lancia|Stratos '73|539,800|
|Mitsubishi|Lancer Evolution VI GSR T.M. SCP '99|165,200|
|Mitsubishi|Lancer Evolution VIII MR GSR '04|65,700|
|Nissan|Sileighty '98|84,800|
|Porsche|911 GT3 (996) '01|161,700|
|Renault|Kangoo 1.4 '01|14,200|
|Renault|R5 Turbo '80|161,400|
|Toyota|Prius G '09|19,400|
