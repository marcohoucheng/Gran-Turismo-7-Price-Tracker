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


# Gran Turismo 7 Shops for 03-April-2025



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Jeep|Willys MB '45|30,100|
|NISMO|400R '95|1,600,000|
|Porsche|911 Carrera RS (901) '73|799,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|GIULIA TZ2 carrozzata da ZAGATO '65|3,800,000|
|Alpine|A220 Race Car '68|330,000|
|Dodge|Challenger R/T '70|214,000|
|Ferrari|330 P4 '67|20,000,000|
|McLaren|MP4/4 '88|12,000,000|
|Mercedes-Benz|Unimog Type 411 '62|46,000|
|Porsche|356 A/1500 GS GT Carrera Speedster '56|1,600,000|
|Shelby|G.T.350 '65|455,000|
|Suzuki|V6 Escudo Pikes Peak Special spec.98|1,700,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Mazda|RX-7 Spirit R Type A (FD) '02|224,600|
|Mitsubishi|Lancer Evolution V GSR '98|65,100|
|Nissan|Silvia Q's (S13) '88|34,200|
|Renault|R5 Turbo '80|160,000|
|Toyota|Supra 3.0GT Turbo A '88|107,400|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Abarth|Abarth 595 SS '70|47,000|
|BMW|3.0 CSL '71|138,000|
|Honda|S2000 '99|98,400|
|Lamborghini|Diablo GT '00|830,900|
|Mitsubishi|Lancer Evolution IX MR GSR '06|97,900|
|Nissan|R33 GT-R V-spec '97|155,200|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|MiTo '09|22,000|
|BMW|M3 '89|76,900|
|BMW|Z4 3.0i '03|53,700|
|Ferrari|512 BB '76|350,000|
|Ferrari|512 BB '76|350,000|
|Honda|Integra Type R (DC2) '98|67,300|
|Honda|S800 '66|42,300|
|Lamborghini|Countach 25th Anniversary '88|655,200|
|Mercedes-Benz|SLR McLaren '09|521,900|
|Nissan|Fairlady 240ZG (HS30) '71|106,400|
|Nissan|R34 GT-R V-spec II Nur '02|388,500|
|Peugeot|205 GTI '88|59,300|
|Porsche|911 Carrera RS (993) '95|215,200|
|RUF|CTR3 '07|788,800|
|Renault|Kangoo 1.4 '01|13,500|
|Subaru|Impreza 22B-STi '98|166,400|
|Subaru|Impreza Coupe WRX Type R STi Ver.VI '99|58,900|
|Subaru|Impreza Sedan WRX STi '04|45,300|
|Suzuki|Cappuccino (EA11R) '91|17,700|
|Toyota|Sprinter Trueno 1600GT APEX (S.Shigeno Version)|104,600|
|Volkswagen|Scirocco R '10|38,700|
|Volkswagen|Volkswagen 1200 '66|29,500|
