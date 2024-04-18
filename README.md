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


# Gran Turismo 7 Shops for 18-April-2024



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|De Tomaso|Mangusta '69|333,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|BMW|McLaren F1 GTR Race Car '97|14,000,000|
|Mercedes-Benz|300 SL (W194) '52|20,000,000|
|Mercedes-Benz|CLK-LM '98|8,500,000|
|Plymouth|Superbird '70|529,000|
|Porsche|356 A/1500 GS GT Carrera Speedster '56|1,500,000|
|Toyota|GT-One (TS020) '99|2,500,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|GIULIA TZ2 carrozzata da ZAGATO '65|3,750,000|
|Alpine|A220 Race Car '68|330,000|
|Chevrolet|Camaro Z28 '69|119,000|
|Citroen|DS 21 Pallas '70|49,600|
|Dodge|Challenger R/T '70|233,000|
|Honda|RA272 '65|2,500,000|
|Shelby|Cobra 427 '66|2,400,000|
|Shelby|G.T.350 '65|460,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Volkswagen|Sambabus Typ 2 '62|57,100|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|BMW|3.0 CSL '73|211,200|
|Honda|Civic Type R (EK) '97|58,100|
|Porsche|911 Carrera RS CS (993) '95|409,500|
|Porsche|911 Turbo (930) '81|215,600|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Abarth|Abarth 500 '09|22,100|
|Alfa Romeo|Giulia Sprint GT Veloce '67|180,000|
|Chevrolet|Corvette Convertible (C3) '69|50,900|
|Dodge|Viper GTS '02|105,600|
|Dodge|Viper SRT10 Coupe '06|115,000|
|Ferrari|512 BB '76|309,000|
|Fiat|500 1.2 8V Lounge SS '08|13,300|
|Ford|Mustang Mach 1 '71|36,800|
|Honda|Beat '91|16,800|
|Honda|Integra Type R (DC2) '98|62,100|
|Honda|NSX Type R '92|398,700|
|Mazda|Eunos Roadster (NA) '89|26,500|
|Mitsubishi|Lancer Evolution IV GSR '96|44,200|
|Mitsubishi|Lancer Evolution IX MR GSR '06|99,700|
|Mitsubishi|Lancer Evolution V GSR '98|77,500|
|Nissan|Fairlady Z (Z34) '08|36,000|
|Nissan|R32 GT-R V-spec II '94|176,500|
|Nissan|Silvia K's Aero (S14) '96|59,300|
|Nissan|Silvia K's Dia Selection (S13) '90|49,700|
|Porsche|911 GT3 (996) '01|155,500|
|Renault|R4 GTL '85|24,100|
|Subaru|Impreza Coupe WRX Type R STi Ver.VI '99|53,600|
|Toyota|Supra 3.0GT Turbo A '88|115,900|
|Volkswagen|Volkswagen 1200 '66|35,800|
