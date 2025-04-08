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


# Gran Turismo 7 Shops for 08-April-2025



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Audi|Sport quattro S1 Pikes Peak '87|1,800,000|
|Jaguar|E-type Coupe '61|218,000|
|Nissan|Skyline 2000GT-R (KPGC110) '73|542,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|GIULIA TZ2 carrozzata da ZAGATO '65|3,800,000|
|Alpine|A220 Race Car '68|330,000|
|Ferrari|330 P4 '67|20,000,000|
|NISMO|400R '95|1,600,000|
|Shelby|G.T.350 '65|455,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Citroen|DS 21 Pallas '70|47,100|
|Jeep|Willys MB '45|30,100|
|Nissan|Skyline Hard Top 2000GT-R (KPGC10) '70|194,000|
|Porsche|911 Carrera RS (901) '73|799,000|
|Suzuki|V6 Escudo Pikes Peak Special spec.98|1,700,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|BMW|3.0 CSL '73|211,200|
|BMW|Z8 '01|259,000|
|Ferrari|308 GTB '75|200,000|
|Ferrari|Testarossa '91|369,000|
|TVR|Tuscan Speed 6 '00|95,000|
|TVR|Tuscan Speed 6 '00|95,000|
|Volkswagen|Sambabus Typ 2 '62|55,600|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|BMW|M3 '89|76,900|
|Honda|Integra Type R (DC2) '98|67,300|
|Honda|S800 '66|42,300|
|Mazda|RX-7 Spirit R Type A (FD) '02|224,600|
|Mercedes-Benz|SLR McLaren '09|521,900|
|Nissan|Fairlady 240ZG (HS30) '71|106,400|
|Porsche|911 Carrera RS (993) '95|215,200|
|Renault|R5 Turbo '80|160,000|
|Subaru|Impreza 22B-STi '98|166,400|
|Subaru|Impreza Sedan WRX STi '04|45,300|
|Toyota|Sprinter Trueno 1600GT APEX (S.Shigeno Version)|104,600|
|Volkswagen|Scirocco R '10|38,700|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|AMG|SLS AMG '10|320,900|
|Alfa Romeo|8C Competizione '08|301,300|
|Maserati|GranTurismo S '08|146,000|
|McLaren|MP4-12C '10|193,900|
|Mitsubishi|Lancer Evolution V GSR '98|65,100|
|Nissan|Silvia K's Aero (S14) '96|59,100|
|Nissan|Silvia K's Dia Selection (S13) '90|51,900|
|Nissan|Silvia Q's (S13) '88|34,200|
|Porsche|911 Turbo (930) '81|224,900|
|Renault|Kangoo 1.4 '01|13,500|
|Renault|R4 GTL '85|26,600|
|Subaru|Impreza Coupe WRX Type R STi Ver.VI '99|58,900|
|Toyota|Prius G '09|20,000|
|Toyota|Supra 3.0GT Turbo A '88|107,400|
|Volkswagen|Volkswagen 1200 '66|29,500|
