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


# Gran Turismo 7 Shops for 19-May-2025



## Legend shop

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Porsche|962 C '88|1,300,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Chaparral|2J '70|2,500,000|
|Chevrolet|Chevelle SS 454 Sport Coupé '70|146,000|
|Chevrolet|Corvette (C1) '58|107,000|
|Chevrolet|Corvette (C1) '58|107,000|
|Chevrolet|Corvette (C2) '63|234,000|
|Ferrari|330 P4 '67|20,000,000|
|Ferrari|500 Mondial Pinin Farina Coupe '54|2,000,000|
|Ford|1932 Ford Roadster Hot Rod|350,000|
|Jaguar|E-type Coupe '61|205,000|
|Porsche|917K '70|18,000,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Ferrari|Testarossa '91|383,800|
|Maserati|GranTurismo S '08|146,000|
|Mazda|Eunos Roadster (NA) '89|30,600|
|Porsche|911 Turbo (930) '81|216,500|
|Toyota|Supra 3.0GT Turbo A '88|116,800|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|8C Competizione '08|301,300|
|BMW|M3 '89|76,900|
|BMW|Z4 3.0i '03|53,700|
|Mazda|RX-7 Spirit R Type A (FD) '02|224,600|
|Mercedes-Benz|SLR McLaren '09|521,900|
|Nissan|Silvia K's Dia Selection (S13) '90|51,900|
|Nissan|Silvia Q's (S13) '88|34,200|
|Porsche|911 Carrera RS (993) '95|215,200|
|Subaru|Impreza Sedan WRX STi '04|45,300|
|Toyota|Prius G '09|20,000|
|Volkswagen|Scirocco R '10|40,600|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|AMG|SLS AMG '10|320,700|
|BMW|3.0 CSL '73|211,200|
|Chevrolet|Corvette Convertible (C3) '69|65,000|
|Chevrolet|Corvette Stingray (C3) '69|71,500|
|Chevrolet|Corvette Z06 (C5) '01|54,200|
|Chevrolet|Corvette ZR-1 (C4) '89|105,000|
|Chevrolet|Corvette ZR1 (C6) '09|97,400|
|Honda|Beat '91|15,400|
|Honda|Civic Si Extra (EF) '87|55,900|
|McLaren|MP4-12C '10|185,500|
|Mitsubishi|Lancer Evolution V GSR '98|73,400|
|Renault|Kangoo 1.4 '01|15,200|
|Subaru|Impreza Coupe WRX Type R STi Ver.VI '99|62,700|
|Volkswagen|Sambabus Typ 2 '62|55,600|
