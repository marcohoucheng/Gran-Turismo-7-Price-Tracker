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


# Gran Turismo 7 Shops for 16-August-2025



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|McLaren|McLaren F1 '94|20,000,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Chevrolet|Corvette (C2) '63|246,000|
|Dodge|Challenger R/T '70|203,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Chaparral|2J '70|2,500,000|
|Chevrolet|Chevelle SS 454 Sport Coupé '70|146,000|
|Ferrari|330 P4 '67|20,000,000|
|Ford|1932 Ford Roadster Hot Rod|350,000|
|Jaguar|E-type Coupe '61|205,000|
|Porsche|917K '70|18,000,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Autobianchi|A112 Abarth '85|29,100|
|Dodge|Super Bee '70|60,200|
|Nissan|Skyline GTS-R (R31) '87|172,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|BMW|M3 '97|80,400|
|Daihatsu|Copen '02|16,100|
|De Tomaso|Pantera '71|200,000|
|Ferrari|Testarossa '91|402,900|
|Ford|Mustang Mach 1 '71|41,400|
|Mitsubishi|GTO Twin Turbo '91|45,700|
|Mitsubishi|Lancer Evolution V GSR '98|77,500|
|Toyota|Supra 3.0GT Turbo A '88|114,400|
|Volkswagen|Golf I GTI '83|42,100|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|Giulia Sprint GT Veloce '67|164,900|
|Alpine|A110 '72|143,800|
|Audi|R8 4.2 '07|141,600|
|BMW|Z8 '01|265,100|
|Chevrolet|Corvette ZR-1 (C4) '89|86,400|
|Chevrolet|Corvette ZR1 (C6) '09|100,800|
|Citroen|BX 19 TRS '87|30,000|
|Citroen|BX 19 TRS '87|30,000|
|Citroen|BX 19 TRS '87|30,000|
|Dodge|Viper SRT10 Coupe '06|111,400|
|Ferrari|Dino 246 GT '71|327,300|
|Honda|Civic Type R (EK) '98|47,000|
|Honda|Civic Type R (EK) Touring Car|122,800|
|Lamborghini|Gallardo LP 560-4 '08|257,000|
|MINI|Mini-Cooper 'S' '65|43,600|
|Mazda|RX-7 GT-X (FC) '90|54,900|
|Pontiac|Firebird Trans Am '78|86,600|
|Porsche|911 Carrera RS CS (993) '95|409,200|
|Suzuki|Swift Sport '07|13,600|
|Toyota|Sprinter Trueno 1600GT APEX (AE86) '83|50,700|
