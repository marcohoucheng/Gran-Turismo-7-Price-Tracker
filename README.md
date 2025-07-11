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


# Gran Turismo 7 Shops for 12-July-2025



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Mercedes-Benz|S Barker Tourer '29|13,000,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Chevrolet|Camaro Z28 '69|115,000|
|De Tomaso|Mangusta '69|325,000|
|Honda|RA272 '65|2,500,000|
|Lancia|Lancia Delta HF Integrale Rally Car '92|300,000|
|Mercedes-Benz|300 SL Coupe '54|1,700,000|
|Mercedes-Benz|Unimog Type 411 '62|46,000|
|Mercedes-Benz|W 196 R '55|20,000,000|
|Shelby|Cobra 427 '66|2,700,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Audi|Sport quattro S1 Pikes Peak '87|1,800,000|
|Honda|NSX GT500 '00|1,500,000|
|Mercedes-Benz|190 E 2.5-16 Evolution II '91|299,000|
|Porsche|Spyder type 550/1500RS '55|4,750,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Ford|Escort RS Cosworth '92|129,800|
|Toyota|Celica GT-Four (ST205) '94|72,300|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Citroen|BX 19 TRS '87|30,000|
|Daihatsu|Copen '02|14,700|
|Honda|Civic Type R (EK) '98|51,300|
|Suzuki|Swift Sport '07|12,900|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|Giulia Sprint GT Veloce '67|164,200|
|Alpine|A110 '72|143,500|
|Audi|R8 4.2 '07|143,600|
|Autobianchi|A112 Abarth '85|30,700|
|Chevrolet|Corvette Convertible (C3) '69|56,000|
|Chevrolet|Corvette ZR1 (C6) '09|103,300|
|Dodge|Super Bee '70|67,800|
|Ferrari|458 Italia '09|251,000|
|Honda|NSX Type R '92|387,000|
|Lamborghini|Gallardo LP 560-4 '08|255,000|
|Lancia|Stratos '73|534,900|
|MINI|Mini-Cooper 'S' '65|39,700|
|Mitsubishi|Lancer Evolution IV GSR '96|41,200|
|Mitsubishi|Lancer Evolution VI GSR T.M. SCP '99|176,100|
|Mitsubishi|Lancer Evolution VIII MR GSR '04|61,800|
|Nissan|R32 GT-R V-spec II '94|171,400|
|Nissan|Sileighty '98|76,500|
|Nissan|Skyline GTS-R (R31) '87|171,900|
|Porsche|911 GT3 (996) '01|155,400|
|Porsche|911 GT3 (997) '09|138,500|
|Toyota|Sprinter Trueno 1600GT APEX (AE86) '83|49,300|
