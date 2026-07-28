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


# Gran Turismo 7 Shops for 28-July-2026



## Legend shop

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Lancia|Lancia Delta HF Integrale Rally Car '92|350,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|155 2.5 V6 TI '93|650,000|
|Ferrari|F50 '95|4,700,000|
|Ford|Mark IV Race Car '67|6,750,000|
|Jaguar|XJ220 '92|548,000|
|Maserati|A6GCS/53 Spyder '54|2,800,000|
|Maserati|Merak SS '80|61,500|
|Nissan|Skyline Super Silhouette Group 5 '84|1,150,000|
|Plymouth|XNR Ghia Roadster '60|3,000,000|
|Renault|Espace F1 '95|2,000,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Abarth|Abarth 500 '09|23,500|
|Honda|NSX Type R '92|396,200|
|Toyota|Corolla Levin 1600GT APEX (AE86) '83|50,200|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Chevrolet|Corvette ZR-1 (C4) '89|88,700|
|Dodge|Viper SRT10 Coupe '06|115,800|
|Honda|S800 '66|49,300|
|Maserati|GranTurismo S '08|147,200|
|Nissan|R32 GT-R V-spec II '94|174,500|
|Nissan|Silvia Q's (S13) '88|28,900|
|Nissan|Skyline GTS-R (R31) '87|171,600|
|Volkswagen|Sambabus Typ 2 '62|56,400|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Audi|R8 4.2 '07|137,900|
|BMW|Z8 '01|266,200|
|Chevrolet|Corvette Convertible (C3) '69|47,000|
|Citroen|BX 19 TRS '87|26,900|
|Ferrari|458 Italia '09|254,300|
|Ferrari|Testarossa '91|372,000|
|Honda|Beat '91|15,000|
|Honda|Civic Si Extra (EF) '87|55,100|
|Lamborghini|Gallardo LP 560-4 '08|251,300|
|Lancia|Stratos '73|539,800|
|Mazda|Eunos Roadster (NA) '89|29,600|
|Mazda|efini RX-7 Type R (FD) '91|66,700|
|McLaren|MP4-12C '10|184,200|
|Mitsubishi|Lancer Evolution IV GSR '96|46,300|
|Mitsubishi|Lancer Evolution VI GSR T.M. SCP '99|165,200|
|Nissan|Sileighty '98|84,800|
|Renault|R4 GTL '85|27,100|
|Subaru|Impreza Coupe WRX Type R STi Ver.VI '99|53,500|
