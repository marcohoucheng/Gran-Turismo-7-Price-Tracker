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


# Gran Turismo 7 Shops for 04-April-2024



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Mercedes-Benz|Sauber Mercedes C9 '89|3,500,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Chevrolet|Corvette Stingray Racer Concept '59|4,000,000|
|Ferrari|F40 '92|3,100,000|
|Ford|Mark IV Race Car '67|6,750,000|
|Jaguar|XJR-9 '88|3,000,000|
|Mazda|787B '91|3,300,000|
|McLaren|MP4/4 '88|10,000,000|
|Renault|R8 Gordini '66|32,500|
|Toyota|GT-One (TS020) '99|2,500,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|AMG|SLS AMG '10|308,300|
|Abarth|Abarth 595 SS '70|57,000|
|Honda|S2000 '99|100,100|
|Renault|R4 GTL '85|30,000|
|Renault|R5 Turbo '80|147,400|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|De Tomaso|Pantera '71|162,200|
|Fiat|500 F '68|17,800|
|Lamborghini|Countach 25th Anniversary '88|711,800|
|Mercedes-Benz|SLR McLaren '09|493,500|
|Nissan|SILVIA spec-R Aero (S15) '02|61,100|
|Porsche|911 Carrera RS (993) '95|215,600|
|Subaru|Impreza 22B-STi '98|170,400|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|Giulia Sprint GT Veloce '67|167,300|
|Alfa Romeo|MiTo '09|22,400|
|BMW|M3 Sport Evolution '89|179,700|
|Ferrari|308 GTB '75|166,400|
|Ferrari|Dino 246 GT '71|400,000|
|Honda|Civic Type R (EK) '98|47,400|
|Honda|Integra Type R (DC2) '95|54,300|
|McLaren|MP4-12C '10|197,300|
|Mitsubishi|Lancer Evolution III GSR '95|87,800|
|Nissan|R34 GT-R V-spec II Nur '02|396,600|
|Nissan|Silvia Q's (S13) '88|31,900|
|RUF|CTR3 '07|801,800|
|Toyota|Prius G '09|21,400|
|Volkswagen|Scirocco R '10|42,000|
