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


# Gran Turismo 7 Shops for 24-July-2026



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Maserati|Merak SS '80|61,500|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Lamborghini|Countach LP400 '74|1,250,000|
|McLaren|MP4/4 '88|12,000,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Jaguar|XJ220 '92|548,000|
|Lancia|Lancia Delta HF Integrale Rally Car '92|350,000|
|Maserati|A6GCS/53 Spyder '54|2,800,000|
|Nissan|Skyline Super Silhouette Group 5 '84|1,150,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Honda|Beat '91|15,000|
|Mitsubishi|Lancer Evolution IV GSR '96|46,300|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|BMW|3.0 CSL '73|205,300|
|Dodge|Super Bee '70|60,500|
|Honda|Civic Type R (EK) Touring Car|115,400|
|Lamborghini|Diablo GT '00|786,300|
|Mitsubishi|Lancer Evolution V GSR '98|64,800|
|Renault|R5 Turbo '80|149,600|
|Toyota|Supra 3.0GT Turbo A '88|116,700|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|BMW|Z8 '01|266,200|
|Chevrolet|Corvette ZR-1 (C4) '89|88,700|
|Citroen|BX 19 TRS '87|26,900|
|Dodge|Viper SRT10 Coupe '06|115,800|
|Ferrari|Testarossa '91|372,000|
|Fiat|Panda 30 CL '85|11,400|
|Honda|S800 '66|49,300|
|Maserati|GranTurismo S '08|147,200|
|Mazda|efini RX-7 Type R (FD) '91|66,700|
|McLaren|MP4-12C '10|184,200|
|Nissan|R32 GT-R V-spec II '94|174,500|
|Nissan|Silvia Q's (S13) '88|28,900|
|Nissan|Skyline GTS-R (R31) '87|171,600|
|Porsche|911 Turbo (930) '81|224,800|
|RUF|CTR3 '07|788,800|
|Renault|R4 GTL '85|27,100|
|Subaru|Impreza Coupe WRX Type R STi Ver.VI '99|53,500|
|Toyota|Prius G '09|19,600|
|Volkswagen|Sambabus Typ 2 '62|56,400|
