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


# Gran Turismo 7 Shops for 31-October-2025



## Legend shop

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Mazda|RX500 '70|600,000|
|Porsche|Carrera GTS (904) '64|2,200,000|
|Toyota|Supra GT500 '97|1,600,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|155 2.5 V6 TI '93|650,000|
|Ferrari|F40 '92|3,200,000|
|Ford|Mark IV Race Car '67|6,750,000|
|Honda|RA272 '65|2,500,000|
|Jaguar|E-type Coupe '61|172,000|
|Jaguar|XJ220 '92|559,000|
|Maserati|A6GCS/53 Spyder '54|2,800,000|
|Maserati|Merak SS '80|61,500|
|Plymouth|XNR Ghia Roadster '60|3,000,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|Giulia Sprint GT Veloce '67|171,300|
|Ferrari|Testarossa '91|365,800|
|Ford|Mustang Mach 1 '71|40,800|
|Honda|Civic Type R (EK) Touring Car|120,700|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Daihatsu|Copen '02|14,400|
|Lamborghini|Diablo GT '00|778,500|
|MINI|Mini-Cooper 'S' '65|38,100|
|Mitsubishi|Lancer Evolution IX MR GSR '06|98,100|
|RUF|CTR3 '07|787,400|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|AMG|SLS AMG '10|320,700|
|Alpine|A110 '72|129,600|
|Autobianchi|A112 Abarth '85|28,200|
|BMW|M3 '97|78,600|
|BMW|Z4 3.0i '03|53,400|
|Chevrolet|Corvette Z06 (C5) '01|57,100|
|Citroen|BX 19 TRS '87|30,000|
|Honda|Civic Type R (EK) '98|55,200|
|Honda|Integra Type R (DC2) '98|55,800|
|Lamborghini|Countach 25th Anniversary '88|687,700|
|Mitsubishi|GTO Twin Turbo '91|55,000|
|Mitsubishi|Lancer Evolution V GSR '98|64,800|
|Nissan|R34 GT-R V-spec II Nur '02|399,800|
|Nissan|Silvia K's Aero (S14) '96|58,800|
|Pontiac|Firebird Trans Am '78|82,700|
|Porsche|911 Turbo (930) '81|223,300|
|Subaru|Impreza Coupe WRX Type R STi Ver.VI '99|52,900|
|Suzuki|Swift Sport '07|12,000|
|Toyota|Sprinter Trueno 1600GT APEX (AE86) '83|53,200|
|Toyota|Sprinter Trueno 1600GT APEX (S.Shigeno Version)|99,500|
|Volkswagen|Golf I GTI '83|49,400|
