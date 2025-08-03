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


# Gran Turismo 7 Shops for 03-August-2025



## Legend shop

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Mazda|RX500 '70|600,000|
|Mercedes-Benz|W 196 R '55|20,000,000|
|Porsche|Carrera GTS (904) '64|2,100,000|
|Toyota|Supra GT500 '97|1,600,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|155 2.5 V6 TI '93|650,000|
|Maserati|A6GCS/53 Spyder '54|2,800,000|
|Maserati|Merak SS '80|64,200|
|Plymouth|XNR Ghia Roadster '60|1,600,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Mazda|Eunos Roadster (NA) '89|27,900|
|RUF|CTR3 '07|792,800|
|Toyota|Corolla Levin 1600GT APEX (AE86) '83|51,800|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|BMW|M3 '89|79,000|
|Chevrolet|Corvette Stingray (C3) '69|64,100|
|Honda|S800 '66|42,300|
|Mazda|RX-7 Spirit R Type A (FD) '02|215,900|
|Nissan|R33 GT-R V-spec '97|154,700|
|Nissan|SILVIA spec-R Aero (S15) '02|59,700|
|Renault|Clio V6 24V '00|100,000|
|Renault|R5 Turbo '80|152,900|
|TVR|Tuscan Speed 6 '00|71,500|
|Toyota|Celica GT-Four (ST205) '94|90,000|
|Volkswagen|Sambabus Typ 2 '62|55,300|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|8C Competizione '08|304,400|
|BMW|M3 Sport Evolution '89|162,400|
|Ford|Sierra RS 500 Cosworth '87|184,900|
|Honda|Beat '91|17,100|
|Honda|Civic Si Extra (EF) '87|57,200|
|Honda|S2000 '99|104,900|
|Mercedes-Benz|SLR McLaren '09|523,400|
|Mitsubishi|Lancer Evolution III GSR '95|83,600|
|Mitsubishi|Lancer Evolution IX MR GSR '06|95,600|
|Porsche|911 Carrera RS (993) '95|233,300|
|Renault|R4 GTL '85|29,200|
|Subaru|Impreza 22B-STi '98|166,900|
|Subaru|Impreza Sedan WRX STi '04|49,900|
|Volkswagen|Scirocco R '10|43,300|
