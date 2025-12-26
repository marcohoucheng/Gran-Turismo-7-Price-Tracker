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


# Gran Turismo 7 Shops for 26-December-2025



## Legend shop

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|GIULIA TZ2 carrozzata da ZAGATO '65|3,850,000|
|Mercedes-Benz|Sauber Mercedes C9 '89|3,500,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alpine|A220 Race Car '68|330,000|
|Ferrari|330 P4 '67|20,000,000|
|Jeep|Willys MB '45|31,300|
|NISMO|400R '95|1,600,000|
|Nissan|Skyline Hard Top 2000GT-R (KPGC10) '70|194,000|
|Porsche|911 Carrera RS (901) '73|740,000|
|Shelby|G.T.350 '65|491,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Renault|Kangoo 1.4 '01|14,200|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|BMW|Z8 '01|267,200|
|Chevrolet|Corvette ZR-1 (C4) '89|84,600|
|Dodge|Super Bee '70|61,100|
|Ferrari|Dino 246 GT '71|359,300|
|Honda|Civic SiR-II (EG) '93|58,500|
|Maserati|GranTurismo S '08|138,200|
|Mitsubishi|GTO Twin Turbo '91|44,800|
|Porsche|911 Carrera RS CS (993) '95|441,300|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Abarth|Abarth 595 SS '70|53,100|
|Alfa Romeo|MiTo '09|22,700|
|Audi|R8 4.2 '07|136,500|
|BMW|3.0 CSL '71|141,800|
|BMW|3.0 CSL '73|205,200|
|Chevrolet|Corvette Convertible (C3) '69|47,000|
|Chevrolet|Corvette ZR1 (C6) '09|99,200|
|Dodge|Viper SRT10 Coupe '06|115,300|
|Fiat|500 F '68|17,900|
|Mitsubishi|Lancer Evolution IV GSR '96|46,300|
|Mitsubishi|Lancer Evolution VI GSR T.M. SCP '99|165,200|
|Nissan|R32 GT-R V-spec II '94|173,400|
|Nissan|Skyline GTS-R (R31) '87|169,000|
