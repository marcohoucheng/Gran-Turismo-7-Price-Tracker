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


# Gran Turismo 7 Shops for 19-December-2024



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Ford|Mark IV Race Car '67|6,750,000|
|Jaguar|XJR-9 '88|3,000,000|
|Mazda|787B '91|3,300,000|
|Mercedes-Benz|Sauber Mercedes C9 '89|3,500,000|
|Nissan|R92CP '92|2,000,000|
|Porsche|962 C '88|1,300,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|155 2.5 V6 TI '93|800,000|
|Chevrolet|Corvette (C1) '58|119,000|
|Ferrari|250 GTO '62|20,000,000|
|Mercedes-Benz|190 E 2.5-16 Evolution II '91|290,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|AMG|300 SEL 6.8 AMG '71|700,000|
|Ferrari|F40 '92|3,100,000|
|Pontiac|GTO 'The Judge' '69|242,000|
|Porsche|Spyder type 550/1500RS '55|4,850,000|
|Renault|R8 Gordini '66|32,500|
|Toyota|2000GT '67|992,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Audi|R8 4.2 '07|137,100|
|Honda|NSX Type R '92|402,700|
|Renault|R5 Turbo '80|151,900|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|BMW|M3 Sport Evolution '89|200,000|
|BMW|M3 Sport Evolution '89|200,000|
|Fiat|500 F '68|15,500|
|Ford|Sierra RS 500 Cosworth '87|200,000|
|Ford|Sierra RS 500 Cosworth '87|200,000|
|Ford|Sierra RS 500 Cosworth '87|200,000|
|Mitsubishi|GTO Twin Turbo '91|41,600|
|Toyota|Sprinter Trueno 1600GT APEX (AE86) '83|51,900|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|Giulia Sprint GT Veloce '67|169,000|
|Alfa Romeo|MiTo '09|22,700|
|BMW|3.0 CSL '73|250,000|
|Chevrolet|Corvette Convertible (C3) '69|53,000|
|Chevrolet|Corvette ZR1 (C6) '09|99,000|
|Dodge|Viper SRT10 Coupe '06|111,800|
|Ferrari|458 Italia '09|242,500|
|Ford|Mustang Mach 1 '71|36,100|
|Honda|Civic Type R (EK) '98|58,100|
|Honda|Civic Type R (EK) Touring Car|114,800|
|Honda|Integra Type R (DC2) '98|61,200|
|MINI|Mini-Cooper 'S' '65|40,800|
|Mitsubishi|Lancer Evolution IV GSR '96|39,600|
|Nissan|R32 GT-R V-spec II '94|178,600|
|Nissan|Silvia Q's (S13) '88|31,800|
|Nissan|Skyline GTS-R (R31) '87|179,600|
|Subaru|Impreza Coupe WRX Type R STi Ver.VI '99|62,300|
|Subaru|Impreza Sedan WRX STi '04|43,600|
|Toyota|Prius G '09|18,500|
