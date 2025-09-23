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


# Gran Turismo 7 Shops for 23-September-2025



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Jaguar|E-type Coupe '61|205,000|
|McLaren|McLaren F1 GTR - BMW '95|16,000,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Ford|GT40 Mark I '66|6,700,000|
|Mazda|787B '91|3,300,000|
|Mercedes-Benz|Unimog Type 411 '62|46,000|
|Plymouth|Superbird '70|402,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|GIULIA TZ2 carrozzata da ZAGATO '65|3,800,000|
|Mercedes-Benz|300 SL (W194) '52|20,000,000|
|NISMO|400R '95|1,600,000|
|NISMO|400R '95|1,600,000|
|Nissan|Skyline 2000GT-R (KPGC110) '73|542,000|
|Nissan|Skyline Hard Top 2000GT-R (KPGC10) '70|194,000|
|Porsche|356 A/1500 GS GT Carrera Speedster '56|1,600,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Autobianchi|A112 Abarth '85|29,100|
|BMW|M3 '97|80,400|
|Ferrari|Dino 246 GT '71|327,300|
|Ford|Mustang Mach 1 '71|41,400|
|Honda|Civic Type R (EK) Touring Car|122,800|
|Porsche|911 Carrera RS CS (993) '95|409,200|
|TVR|Tuscan Speed 6 '00|95,000|
|TVR|Tuscan Speed 6 '00|95,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|BMW|Z4 3.0i '03|43,700|
|Chevrolet|Corvette Z06 (C5) '01|50,200|
|Daihatsu|Copen '02|16,100|
|Nissan|R34 GT-R V-spec II Nur '02|387,000|
|Pontiac|Firebird Trans Am '78|86,600|
|Toyota|Sprinter Trueno 1600GT APEX (S.Shigeno Version)|99,200|
|Volkswagen|Golf I GTI '83|42,100|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|AMG|SLS AMG '10|315,900|
|Alfa Romeo|Giulia Sprint GT Veloce '67|164,900|
|Alpine|A110 '72|143,800|
|BMW|Z8 '01|265,100|
|Ferrari|Testarossa '91|402,900|
|Honda|Civic Type R (EK) '98|47,000|
|MINI|Mini-Cooper 'S' '65|43,600|
|Maserati|GranTurismo S '08|137,900|
|McLaren|MP4-12C '10|187,100|
|Mitsubishi|GTO Twin Turbo '91|45,700|
|Mitsubishi|Lancer Evolution V GSR '98|77,500|
|Nissan|GT-R NISMO (R32) '90|400,000|
|Nissan|R32 GT-R V-spec II '94|200,000|
|Nissan|R33 GT-R V-spec '97|180,000|
|Nissan|Silvia K's Aero (S14) '96|57,700|
|Porsche|911 Turbo (930) '81|223,900|
|Subaru|Impreza Coupe WRX Type R STi Ver.VI '99|52,500|
|Suzuki|Swift Sport '07|13,600|
|Toyota|Sprinter Trueno 1600GT APEX (AE86) '83|50,700|
|Toyota|Supra 3.0GT Turbo A '88|114,400|
