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


# Gran Turismo 7 Shops for 17-June-2024



## Legend shop

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|De Tomaso|Mangusta (Christian Dior)|500,000|
|Ferrari|365 GTB4 '71|610,000|
|Mercedes-Benz|CLK-LM '98|8,500,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Abarth|1500 Biposto Bertone B.A.T 1 '52|1,000,000|
|Alfa Romeo|8C 2900B Touring Berlinetta '38|20,000,000|
|BMW|McLaren F1 GTR Race Car '97|20,000,000|
|Ferrari|F40 '92|3,100,000|
|Ferrari|F50 '95|4,450,000|
|Ford|Mustang Boss 429 '69|346,000|
|Nissan|Skyline 2000GT-R (KPGC110) '73|542,000|
|Peugeot|205 Turbo 16 Evolution 2 '86|1,100,000|
|Toyota|Celica GT-FOUR Rally Car (ST205) '95|250,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Fiat|500 1.2 8V Lounge SS '08|13,300|
|Honda|Beat '91|16,800|
|Mitsubishi|GTO Twin Turbo '91|40,000|
|Nissan|Silvia K's Dia Selection (S13) '90|49,700|
|Porsche|911 Turbo (930) '81|215,600|
|Volkswagen|Volkswagen 1200 '66|35,800|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|8C Competizione '08|287,200|
|BMW|M3 Sport Evolution '89|179,700|
|Chevrolet|Corvette ZR-1 (C4) '89|86,100|
|Lamborghini|Diablo GT '00|789,300|
|Lancia|Delta HF Integrale Evoluzione '91|101,900|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Audi|R8 4.2 '07|137,600|
|BMW|3.0 CSL '71|141,500|
|BMW|3.0 CSL '73|211,200|
|Chevrolet|Corvette ZR1 (C6) '09|98,400|
|Dodge|Super Bee '70|71,900|
|Ferrari|Dino 246 GT '71|343,900|
|Ford|Sierra RS 500 Cosworth '87|193,500|
|Honda|Civic SiR-II (EG) '93|52,100|
|Honda|Civic Type R (EK) '97|58,100|
|Honda|S2000 '99|100,100|
|Lamborghini|Countach 25th Anniversary '88|711,800|
|Mazda|Eunos Roadster (NA) '89|26,500|
|Mercedes-Benz|SLR McLaren '09|493,500|
|Nissan|Fairlady 240ZG (HS30) '71|98,500|
|Nissan|R33 GT-R V-spec '97|155,200|
|Nissan|Sileighty '98|72,400|
|Nissan|Skyline GTS-R (R31) '87|176,600|
|Subaru|Impreza Sedan WRX STi '04|47,100|
|Toyota|Sprinter Trueno 1600GT APEX (S.Shigeno Version)|97,800|
|Volvo|240 SE Estate '93|40,800|
