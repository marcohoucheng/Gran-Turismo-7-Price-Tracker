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


# Gran Turismo 7 Shops for 21-June-2025



## Legend shop

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Chevrolet|Corvette Stingray Racer Concept '59|4,000,000|
|Ford|Mark IV Race Car '67|6,750,000|
|Shelby|Cobra Daytona Coupe '64|20,000,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Ferrari|GTO '84|3,500,000|
|Ford|GT40 Mark I '66|6,700,000|
|Lamborghini|Miura P400 Bertone Prototype '67|4,300,000|
|Mazda|787B '91|3,300,000|
|Mercedes-Benz|Sauber Mercedes C9 '89|3,500,000|
|Plymouth|Superbird '70|402,000|
|Subaru|Impreza Rally Car '98|650,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|BMW|3.0 CSL '73|211,000|
|Lamborghini|Diablo GT '00|772,200|
|Mitsubishi|Lancer Evolution IX MR GSR '06|95,800|
|Renault|Kangoo 1.4 '01|15,200|
|Subaru|Impreza Sedan WRX STi '04|40,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|BMW|M3 '97|90,000|
|Nissan|R33 GT-R V-spec '97|160,500|
|Nissan|SILVIA spec-R Aero (S15) '02|58,200|
|TVR|Tuscan Speed 6 '00|73,200|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|BMW|M3 '89|82,300|
|Ford|Sierra RS 500 Cosworth '87|198,900|
|Honda|Integra Type R (DC2) '98|65,500|
|Honda|S2000 '99|99,400|
|Honda|S800 '66|52,100|
|Mazda|RX-7 Spirit R Type A (FD) '02|215,300|
|Mercedes-Benz|SLR McLaren '09|492,000|
|Mitsubishi|Lancer Evolution III GSR '95|87,300|
|Nissan|Fairlady 240ZG (HS30) '71|102,800|
|Nissan|R34 GT-R V-spec II Nur '02|399,800|
|Nissan|Silvia K's Dia Selection (S13) '90|48,900|
|Nissan|Silvia Q's (S13) '88|28,800|
|Porsche|911 Carrera RS (993) '95|229,200|
|RUF|CTR3 '07|805,400|
|Renault|R4 GTL '85|27,300|
|Renault|R5 Turbo '80|157,500|
|Toyota|Prius G '09|19,600|
|Toyota|Sprinter Trueno 1600GT APEX (S.Shigeno Version)|99,500|
|Volkswagen|Sambabus Typ 2 '62|56,400|
|Volkswagen|Scirocco R '10|39,500|
