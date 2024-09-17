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


# Gran Turismo 7 Shops for 17-September-2024



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Aston Martin|DB5 '64|892,000|
|Jaguar|XJR-9 '88|3,000,000|
|Toyota|2000GT '67|992,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Peugeot|205 Turbo 16 Evolution 2 '86|1,100,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|BMW|McLaren F1 GTR Race Car '97|20,000,000|
|Chevrolet|Corvette (C1) '58|119,000|
|Ferrari|250 GTO '62|20,000,000|
|Ford|Mustang Boss 429 '69|346,000|
|Jaguar|XJ13 '66|12,000,000|
|Porsche|356 A/1500 GS Carrera '56|618,000|
|Porsche|356 A/1500 GS GT Carrera Speedster '56|1,600,000|
|Suzuki|V6 Escudo Pikes Peak Special spec.98|1,700,000|
|Toyota|Celica GT-FOUR Rally Car (ST205) '95|250,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Ferrari|512 BB '76|350,000|
|Nissan|SILVIA spec-R Aero (S15) '02|59,900|
|Suzuki|Cappuccino (EA11R) '91|16,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Honda|Civic Type R (EK) '98|58,100|
|Mazda|RX-7 Spirit R Type A (FD) '02|216,300|
|Mercedes-Benz|SLR McLaren '09|495,200|
|Mitsubishi|Lancer Evolution IX MR GSR '06|91,400|
|Nissan|Fairlady Z 300ZX TT 2seater '89|52,500|
|Renault|Clio V6 24V '00|81,900|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Abarth|Abarth 595 SS '70|58,200|
|Alfa Romeo|8C Competizione '08|290,200|
|Audi|TT Coupe 3.2 quattro '03|42,100|
|Autobianchi|A112 Abarth '85|29,800|
|BMW|M3 '89|86,100|
|Chevrolet|Corvette Stingray (C3) '69|63,100|
|De Tomaso|Pantera '71|170,400|
|Honda|Integra Type R (DC2) '95|62,300|
|Honda|S800 '66|48,700|
|Lamborghini|Countach 25th Anniversary '88|701,600|
|Lamborghini|Diablo GT '00|779,000|
|Lancia|Delta HF Integrale Evoluzione '91|98,900|
|Nissan|R33 GT-R V-spec '97|154,300|
|Nissan|Silvia Q's (S13) '88|31,800|
|Porsche|911 Carrera RS (993) '95|229,200|
|Renault|R5 Turbo '80|151,900|
|Subaru|Impreza 22B-STi '98|176,100|
|Toyota|MR2 GT-S '97|53,600|
|Toyota|Sprinter Trueno 1600GT APEX (S.Shigeno Version)|106,700|
