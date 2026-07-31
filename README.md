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


# Gran Turismo 7 Shops for 31-July-2026



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Porsche|959 '87|1,950,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Maserati|Merak SS '80|61,500|
|NISMO|400R '95|1,300,000|
|Nissan|Skyline 2000GT-R (KPGC110) '73|537,000|
|Nissan|Skyline Hard Top 2000GT-R (KPGC10) '70|194,000|
|Plymouth|XNR Ghia Roadster '60|3,000,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|155 2.5 V6 TI '93|650,000|
|Ferrari|365 GTB4 '71|595,000|
|Ferrari|F50 '95|4,700,000|
|Ford|Mark IV Race Car '67|6,750,000|
|Nissan|Fairlady Z 432 '69|312,000|
|Renault|Espace F1 '95|2,000,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Fiat|500 1.2 8V Lounge SS '08|12,500|
|Mitsubishi|FTO GP Version R '97|26,200|
|Porsche|911 GT3 (997) '09|141,900|
|Toyota|Celica GT-Four (ST205) '94|65,500|
|Toyota|Sports 800 '65|43,800|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|BMW|Z8 '01|266,200|
|Chevrolet|Corvette Convertible (C3) '69|47,000|
|Ferrari|Testarossa '91|372,000|
|Honda|Civic Si Extra (EF) '87|55,100|
|Lamborghini|Gallardo LP 560-4 '08|251,300|
|Mazda|Eunos Roadster (NA) '89|29,600|
|Mazda|efini RX-7 Type R (FD) '91|66,700|
|Mitsubishi|Lancer Evolution IV GSR '96|46,300|
|Nissan|GT-R NISMO (R32) '90|400,000|
|Nissan|R32 GT-R V-spec II '94|200,000|
|Nissan|R33 GT-R V-spec '97|180,000|
|Subaru|Impreza Coupe WRX Type R STi Ver.VI '99|53,500|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Abarth|Abarth 500 '09|23,500|
|Audi|R8 4.2 '07|137,900|
|Autobianchi|A112 Abarth '85|39,000|
|Ferrari|458 Italia '09|254,300|
|Ford|Escort RS Cosworth '92|128,900|
|Honda|Beat '91|15,000|
|Honda|NSX Type R '92|396,200|
|Lancia|Stratos '73|539,800|
|McLaren|MP4-12C '10|184,200|
|Mitsubishi|Lancer Evolution VI GSR T.M. SCP '99|165,200|
|Mitsubishi|Lancer Evolution VIII MR GSR '04|69,200|
|Nissan|Sileighty '98|84,800|
|Porsche|911 GT3 (996) '01|158,500|
|Renault|R4 GTL '85|27,100|
|TVR|Tuscan Speed 6 '00|95,000|
|Toyota|Corolla Levin 1600GT APEX (AE86) '83|50,200|
|Volvo|240 SE Estate '93|48,600|
