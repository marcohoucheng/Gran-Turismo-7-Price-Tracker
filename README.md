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


# Gran Turismo 7 Shops for 16-July-2025



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Shelby|Cobra Daytona Coupe '64|20,000,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Porsche|Spyder type 550/1500RS '55|4,750,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Dodge|Charger R/T 426 Hemi '68|154,000|
|Honda|NSX GT500 '00|1,500,000|
|McLaren|McLaren F1 GTR - BMW '95|16,000,000|
|Mercedes-Benz|300 SL Coupe '54|1,700,000|
|Mercedes-Benz|S Barker Tourer '29|13,000,000|
|Nissan|Fairlady Z 432 '69|312,000|
|Nissan|GT-R GT500 '99|2,200,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|BMW|3.0 CSL '71|148,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Audi|R8 4.2 '07|143,600|
|Autobianchi|A112 Abarth '85|30,700|
|Chevrolet|Corvette Convertible (C3) '69|56,000|
|Ferrari|458 Italia '09|251,000|
|Honda|NSX Type R '92|387,000|
|MINI|Mini-Cooper 'S' '65|39,700|
|Mitsubishi|Lancer Evolution IV GSR '96|41,200|
|Nissan|R32 GT-R V-spec II '94|171,400|
|Nissan|Skyline GTS-R (R31) '87|171,900|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Abarth|Abarth 595 SS '70|47,000|
|Fiat|500 F '68|16,000|
|Ford|Escort RS Cosworth '92|129,800|
|Honda|Civic SiR-II (EG) '93|56,000|
|Lamborghini|Murcielago LP 640 '09|329,700|
|Lancia|Delta HF Integrale Evoluzione '91|107,800|
|Lancia|Stratos '73|534,900|
|Mitsubishi|Lancer Evolution VI GSR T.M. SCP '99|176,100|
|Mitsubishi|Lancer Evolution VIII MR GSR '04|61,800|
|Nissan|Fairlady Z (Z34) '08|32,900|
|Nissan|Sileighty '98|76,500|
|Nissan|Silvia K's Type S (S14) '94|44,900|
|Porsche|911 GT3 (996) '01|155,400|
|Porsche|911 GT3 (997) '09|138,500|
|Toyota|Celica GT-Four (ST205) '94|72,300|
|Toyota|Sprinter Trueno 1600GT APEX (AE86) '83|49,300|
