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


# Gran Turismo 7 Shops for 04-November-2025



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Chevrolet|Corvette (C2) '63|268,000|
|Dodge|Challenger R/T '70|179,000|
|Plymouth|Superbird '70|450,000|
|Porsche|911 GT1 Strassenversion '97|10,000,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Ferrari|F50 '95|4,600,000|
|Ford|Mark IV Race Car '67|6,750,000|
|Honda|RA272 '65|2,500,000|
|Jaguar|XJ220 '92|559,000|
|Plymouth|XNR Ghia Roadster '60|3,000,000|
|Porsche|356 A/1500 GS Carrera '56|618,000|
|Porsche|959 '87|1,900,000|
|Porsche|962 C '88|1,250,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|BMW|Z8 '01|267,200|
|Chevrolet|Corvette Convertible (C3) '69|65,000|
|Dodge|Viper SRT10 Coupe '06|115,300|
|Mazda|RX-7 GT-X (FC) '90|62,800|
|Mitsubishi|GTO Twin Turbo '91|44,800|
|Nissan|Silvia K's Type S (S14) '94|50,800|
|Peugeot|205 GTI '88|54,100|
|Pontiac|Firebird Trans Am '78|110,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alpine|A110 '72|129,600|
|Honda|Civic Type R (EK) '98|55,200|
|Subaru|Impreza Coupe WRX Type R STi Ver.VI '99|52,900|
|Volkswagen|Golf I GTI '83|49,400|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|AMG|SLS AMG '10|320,700|
|Alfa Romeo|Giulia Sprint GT Veloce '67|171,300|
|Autobianchi|A112 Abarth '85|28,200|
|BMW|M3 '97|78,600|
|Ferrari|Dino 246 GT '71|359,300|
|Ferrari|Testarossa '91|365,800|
|Ford|Mustang Mach 1 '71|40,800|
|Honda|Civic Type R (EK) Touring Car|120,700|
|Lancia|Delta HF Integrale Evoluzione '91|101,200|
|Maserati|GranTurismo S '08|138,200|
|McLaren|MP4-12C '10|185,500|
|Mitsubishi|Lancer Evolution V GSR '98|64,800|
|Nissan|Silvia K's Aero (S14) '96|58,800|
|Porsche|911 Carrera RS CS (993) '95|441,300|
|Porsche|911 Turbo (930) '81|223,300|
|Renault|Avantime 3.0 V6 24V '02|37,600|
|Toyota|Sprinter Trueno 1600GT APEX (AE86) '83|53,200|
|Toyota|Supra 3.0GT Turbo A '88|105,400|
