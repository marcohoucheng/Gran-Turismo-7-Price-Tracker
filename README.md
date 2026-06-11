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


# Gran Turismo 7 Shops for 11-June-2026



## Legend shop

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Chevrolet|Corvette Stingray Racer Concept '59|7,000,000|
|Pontiac|GTO 'The Judge' '69|196,000|
|Renault|R8 Gordini '66|32,500|
|Toyota|Land Cruiser FJ40V '74|50,900|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Aston Martin|DB5 '64|883,000|
|Ford|Mark IV Race Car '67|6,750,000|
|Lamborghini|Miura P400 Bertone Prototype '67|4,300,000|
|McLaren|McLaren F1 '94|20,000,000|
|Mercedes-Benz|Unimog Type 411 '62|46,000|
|Nissan|R92CP '92|2,000,000|
|Porsche|356 A/1500 GS GT Carrera Speedster '56|1,400,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Chevrolet|Corvette ZR-1 (C4) '89|86,500|
|Mazda|efini RX-7 Type R (FD) '91|69,600|
|Nissan|R32 GT-R V-spec II '94|173,400|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|AMG|SLS AMG '10|319,400|
|BMW|3.0 CSL '73|206,600|
|Honda|Civic Type R (EK) Touring Car|123,400|
|Porsche|911 Turbo (930) '81|213,800|
|Toyota|Supra 3.0GT Turbo A '88|116,800|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|Giulia Sprint GT Veloce '67|180,000|
|BMW|Z8 '01|269,600|
|Citroen|BX 19 TRS '87|23,100|
|Dodge|Super Bee '70|61,100|
|Dodge|Viper SRT10 Coupe '06|114,400|
|Ferrari|Testarossa '91|368,500|
|Honda|S2000 '99|120,000|
|Honda|S800 '66|42,300|
|Lamborghini|Diablo GT '00|785,300|
|Maserati|GranTurismo S '08|138,200|
|McLaren|MP4-12C '10|195,700|
|Mitsubishi|Lancer Evolution V GSR '98|73,400|
|Nissan|R34 GT-R V-spec II Nur '02|398,700|
|Nissan|Silvia Q's (S13) '88|34,900|
|Nissan|Skyline GTS-R (R31) '87|169,000|
|Renault|Kangoo 1.4 '01|14,100|
|Renault|R4 GTL '85|29,200|
|Renault|R5 Turbo '80|152,900|
|Subaru|Impreza Coupe WRX Type R STi Ver.VI '99|62,700|
|Toyota|Prius G '09|20,700|
|Volkswagen|Sambabus Typ 2 '62|55,300|
