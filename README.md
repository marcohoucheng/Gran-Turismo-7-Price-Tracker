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


# Gran Turismo 7 Shops for 31-March-2024



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Renault|R8 Gordini '66|32,500|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Ferrari|250 GTO '62|20,000,000|
|Nissan|GT-R GT500 '99|2,700,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|AMG|300 SEL 6.8 AMG '71|700,000|
|Chevrolet|Corvette (C1) '58|121,000|
|Ferrari|F40 '92|3,100,000|
|Ford|Mark IV Race Car '67|6,750,000|
|Jaguar|XJR-9 '88|3,000,000|
|Pontiac|GTO 'The Judge' '69|279,000|
|Toyota|2000GT '67|936,000|
|Toyota|GT-One (TS020) '99|2,500,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|Giulia Sprint GT Veloce '67|167,300|
|Fiat|500 F '68|17,800|
|McLaren|MP4-12C '10|197,300|
|Nissan|SILVIA spec-R Aero (S15) '02|61,100|
|Nissan|Silvia Q's (S13) '88|31,900|
|Porsche|911 Carrera RS (993) '95|215,600|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|BMW|3.0 CSL '73|250,000|
|Chevrolet|Corvette ZR1 (C6) '09|104,900|
|MINI|Mini-Cooper 'S' '65|38,200|
|Toyota|Sprinter Trueno 1600GT APEX (S.Shigeno Version)|105,900|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|MiTo '09|22,400|
|Alpine|A110 '72|132,900|
|Audi|R8 4.2 '07|137,800|
|Chevrolet|Corvette Stingray (C3) '69|59,200|
|Chevrolet|Corvette ZR-1 (C4) '89|86,500|
|Daihatsu|Copen '02|13,400|
|De Tomaso|Pantera '71|162,200|
|Honda|Integra Type R (DC2) '95|54,300|
|Honda|NSX Type R '02|430,000|
|Lamborghini|Countach 25th Anniversary '88|711,800|
|Mercedes-Benz|SLR McLaren '09|493,500|
|Nissan|R33 GT-R V-spec '97|156,200|
|Subaru|Impreza 22B-STi '98|170,400|
|Toyota|MR2 GT-S '97|51,500|
|Toyota|Sports 800 '65|43,200|
|Toyota|Sprinter Trueno 1600GT APEX (AE86) '83|48,900|
