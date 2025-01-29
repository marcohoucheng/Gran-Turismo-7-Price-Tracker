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


# Gran Turismo 7 Shops for 29-January-2025



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Toyota|GT-One (TS020) '99|2,500,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Dodge|Charger R/T 426 Hemi '68|158,000|
|Jaguar|XJ13 '66|12,000,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Aston Martin|DB5 '64|892,000|
|Ferrari|250 GT Berlinetta passo corto '61|7,800,000|
|Jaguar|E-type Coupe '61|218,000|
|Nissan|Fairlady Z 432 '69|312,000|
|Nissan|GT-R GT500 '99|2,500,000|
|Shelby|Cobra Daytona Coupe '64|20,000,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Chevrolet|Corvette ZR-1 (C4) '89|90,600|
|Ferrari|Dino 246 GT '71|333,900|
|Lamborghini|Gallardo LP 560-4 '08|249,200|
|Mazda|RX-7 GT-X (FC) '90|58,900|
|Mitsubishi|Lancer Evolution VI GSR T.M. SCP '99|162,400|
|Porsche|911 Carrera RS CS (993) '95|438,500|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Chevrolet|Corvette Convertible (C3) '69|53,000|
|Ferrari|458 Italia '09|242,500|
|Honda|S800 '66|48,700|
|Mitsubishi|Lancer Evolution IV GSR '96|39,600|
|Nissan|R32 GT-R V-spec II '94|178,600|
|Renault|R5 Turbo '80|151,900|
|Suzuki|Cappuccino (EA11R) '91|16,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Audi|R8 4.2 '07|137,100|
|BMW|3.0 CSL '71|140,400|
|Chevrolet|Corvette ZR1 (C6) '09|99,000|
|Dodge|Super Bee '70|63,200|
|Dodge|Viper SRT10 Coupe '06|111,800|
|Ferrari|512 BB '76|350,000|
|Honda|Civic SiR-II (EG) '93|50,800|
|Honda|Civic Type R (EK) Touring Car|114,800|
|Honda|NSX Type R '92|402,700|
|Lancia|Delta HF Integrale Evoluzione '91|98,900|
|Lancia|Stratos '73|499,300|
|Nissan|Fairlady 240ZG (HS30) '71|106,400|
|Nissan|Sileighty '98|89,700|
|Nissan|Skyline GTS-R (R31) '87|179,600|
|Porsche|911 GT3 (996) '01|155,600|
|Volkswagen|Volkswagen 1200 '66|28,800|
