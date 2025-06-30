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


# Gran Turismo 7 Shops for 30-June-2025



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Jeep|Willys MB '45|33,100|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Dodge|Challenger R/T '70|203,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|GIULIA TZ2 carrozzata da ZAGATO '65|3,800,000|
|Alpine|A220 Race Car '68|330,000|
|Ferrari|330 P4 '67|20,000,000|
|Lancia|Lancia Delta HF Integrale Rally Car '92|300,000|
|Mercedes-Benz|300 SL Coupe '54|1,700,000|
|Mercedes-Benz|Unimog Type 411 '62|46,000|
|Mercedes-Benz|W 196 R '55|20,000,000|
|NISMO|400R '95|1,600,000|
|Porsche|911 Carrera RS (901) '73|799,000|
|Shelby|G.T.350 '65|455,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|AMG|SLS AMG '10|319,400|
|Fiat|500 1.2 8V Lounge SS '08|12,500|
|Maserati|GranTurismo S '08|142,400|
|Mitsubishi|GTO Twin Turbo '91|42,300|
|Nissan|Silvia K's Aero (S14) '96|58,100|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|8C Competizione '08|289,700|
|BMW|3.0 CSL '73|211,000|
|BMW|M3 Sport Evolution '89|162,200|
|BMW|Z4 3.0i '03|48,900|
|Lamborghini|Countach 25th Anniversary '88|706,200|
|Porsche|911 Carrera RS (993) '95|229,200|
|Subaru|Impreza 22B-STi '98|173,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Abarth|Abarth 500 '09|23,500|
|Chevrolet|Corvette Z06 (C5) '01|48,700|
|Citroen|BX 19 TRS '87|30,000|
|Honda|Beat '91|15,400|
|Honda|Civic Si Extra (EF) '87|55,900|
|Mazda|Eunos Roadster (NA) '89|29,600|
|McLaren|MP4-12C '10|198,400|
|Mitsubishi|Lancer Evolution V GSR '98|73,400|
|Porsche|911 Turbo (930) '81|216,500|
|Subaru|Impreza Coupe WRX Type R STi Ver.VI '99|62,700|
|Toyota|Corolla Levin 1600GT APEX (AE86) '83|50,200|
|Toyota|Sports 800 '65|43,800|
|Toyota|Supra 3.0GT Turbo A '88|116,800|
|Volvo|240 SE Estate '93|48,600|
