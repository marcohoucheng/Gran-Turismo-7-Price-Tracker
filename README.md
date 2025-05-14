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


# Gran Turismo 7 Shops for 14-May-2025



## Legend shop

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|155 2.5 V6 TI '93|800,000|
|Ferrari|F50 '95|4,450,000|
|Jaguar|XJ220 '92|554,000|
|Porsche|959 '87|1,950,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Aston Martin|DB5 '64|892,000|
|Ford|Mark IV Race Car '67|6,750,000|
|Plymouth|XNR Ghia Roadster '60|1,600,000|
|Porsche|356 A/1500 GS Carrera '56|618,000|
|Porsche|911 GT1 Strassenversion '97|10,000,000|
|Porsche|962 C '88|1,300,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|8C Competizione '08|301,300|
|BMW|M3 '89|76,900|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|BMW|M3 Sport Evolution '89|162,000|
|Mitsubishi|Lancer Evolution IX MR GSR '06|97,900|
|Nissan|Fairlady 240ZG (HS30) '71|106,400|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|BMW|Z4 3.0i '03|53,700|
|Ford|Sierra RS 500 Cosworth '87|190,600|
|Honda|Civic Si Extra (EF) '87|70,000|
|Honda|Civic SiR-II (EG) '93|60,000|
|Honda|Civic Type R (EK) '97|65,000|
|Honda|Civic Type R (EK) '98|65,000|
|Honda|Civic Type R (EK) Touring Car|140,000|
|Honda|Integra Type R (DC2) '98|67,300|
|Honda|S2000 '99|97,300|
|Honda|S800 '66|42,300|
|Lamborghini|Countach 25th Anniversary '88|655,200|
|Lamborghini|Diablo GT '00|830,900|
|Mazda|RX-7 Spirit R Type A (FD) '02|224,600|
|Mercedes-Benz|SLR McLaren '09|521,900|
|Mitsubishi|Lancer Evolution III GSR '95|92,200|
|Nissan|R34 GT-R V-spec II Nur '02|388,500|
|Nissan|Silvia K's Dia Selection (S13) '90|51,900|
|Nissan|Silvia Q's (S13) '88|34,200|
|Porsche|911 Carrera RS (993) '95|215,200|
|RUF|CTR3 '07|788,800|
|Renault|R4 GTL '85|26,600|
|Renault|R5 Turbo '80|160,000|
|Subaru|Impreza 22B-STi '98|166,400|
|Subaru|Impreza Sedan WRX STi '04|45,300|
|Toyota|Prius G '09|20,000|
|Toyota|Sprinter Trueno 1600GT APEX (S.Shigeno Version)|104,600|
|Volkswagen|Scirocco R '10|40,600|
|Volkswagen|Volkswagen 1200 '66|29,500|
