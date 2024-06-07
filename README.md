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


# Gran Turismo 7 Shops for 07-June-2024



## Legend shop

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Porsche|917K '70|18,000,000|
|Porsche|962 C '88|1,500,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Aston Martin|DB3S '53|6,000,000|
|BMW|McLaren F1 GTR Race Car '97|20,000,000|
|Chaparral|2J '70|2,500,000|
|Chevrolet|Chevelle SS 454 Sport Coupé '70|172,000|
|Ferrari|330 P4 '67|20,000,000|
|Ferrari|F40 '92|3,100,000|
|Ford|1932 Ford Roadster Hot Rod|400,000|
|Honda|NSX GT500 '00|1,500,000|
|Jaguar|E-type Coupe '61|227,000|
|McLaren|McLaren F1 '94|20,000,000|
|McLaren|McLaren F1 GTR - BMW '95|15,000,000|
|Nissan|GT-R GT500 '99|2,500,000|
|Toyota|Supra GT500 '97|1,800,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Abarth|Abarth 595 SS '70|57,000|
|Audi|R8 4.2 '07|137,600|
|BMW|M3 Sport Evolution '89|179,700|
|Honda|S800 '66|49,600|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|Giulia Sprint GT Veloce '67|167,300|
|Audi|TTS Coupe '09|63,100|
|BMW|M3 '07|69,900|
|BMW|M3 '89|75,700|
|Ferrari|F430 '06|201,100|
|Honda|Beat '91|20,000|
|Porsche|911 Carrera RS (964) '92|226,500|
|Subaru|Impreza 22B-STi '98|177,300|
|Suzuki|Cappuccino (EA11R) '91|20,000|
|TVR|Tuscan Speed 6 '00|72,500|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|MiTo '09|22,400|
|BMW|M3 '03|72,800|
|Chevrolet|Corvette ZR-1 (C4) '89|86,100|
|De Tomaso|Pantera '71|162,200|
|Honda|Civic SiR-II (EG) '93|52,100|
|Honda|Civic Type R (EK) '98|47,400|
|Honda|Integra Type R (DC2) '95|61,200|
|Honda|NSX Type R '02|431,600|
|Lamborghini|Diablo GT '00|789,300|
|Nissan|GT-R NISMO (R32) '90|390,000|
|Nissan|SILVIA spec-R Aero (S15) '02|61,100|
|Nissan|Silvia Q's (S13) '88|31,900|
|Nissan|Skyline GTS-R (R31) '87|176,600|
|Porsche|911 Carrera RS (993) '95|260,000|
|Renault|R5 Turbo '80|147,400|
|Toyota|MR2 GT-S '97|58,100|
|Toyota|Prius G '09|21,400|
|Volkswagen|Scirocco R '10|42,000|
|Volvo|240 SE Estate '93|40,800|
