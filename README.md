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


# Gran Turismo 7 Shops for 27-July-2025



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Porsche|Carrera GTS (904) '64|2,100,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Aston Martin|DB5 '64|909,000|
|Ferrari|250 GT Berlinetta passo corto '61|7,000,000|
|Pontiac|GTO 'The Judge' '69|242,000|
|Porsche|911 GT1 Strassenversion '97|10,000,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Lancia|Lancia Delta HF Integrale Rally Car '92|300,000|
|McLaren|MP4/4 '88|12,000,000|
|Mercedes-Benz|W 196 R '55|20,000,000|
|Nissan|Skyline Super Silhouette Group 5 '84|1,150,000|
|Toyota|GT-One (TS020) '99|2,500,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Chevrolet|Corvette Stingray (C3) '69|64,100|
|Ford|Sierra RS 500 Cosworth '87|184,900|
|Honda|S800 '66|42,300|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Audi|TTS Coupe '09|62,200|
|BMW|M3 '07|74,300|
|Ferrari|308 GTB '75|165,100|
|Ferrari|430 Scuderia '07|375,600|
|Honda|Integra Type R (DC2) '95|55,600|
|Honda|NSX Type R '02|435,000|
|Nissan|Fairlady Z 300ZX TT 2seater '89|60,700|
|Nissan|Silvia K's Dia Selection (S13) '90|49,500|
|Pontiac|Firebird Trans Am '78|110,000|
|Porsche|911 Turbo (930) '81|250,000|
|Toyota|MR2 GT-S '97|51,100|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|BMW|3.0 CSL '73|212,700|
|BMW|M3 '03|72,500|
|Citroen|BX 19 TRS '87|23,100|
|De Tomaso|Pantera '71|165,000|
|Ferrari|F430 '06|212,700|
|Nissan|Fairlady 240ZG (HS30) '71|97,200|
|Nissan|GT-R NISMO (R32) '90|389,500|
|Nissan|SILVIA spec-R Aero (S15) '02|59,700|
|Nissan|Silvia Q's (S13) '88|34,900|
|Porsche|911 Carrera RS (964) '92|216,000|
|Renault|Kangoo 1.4 '01|13,300|
|Renault|R5 Turbo '80|152,900|
|Toyota|Celica GT-Four (ST205) '94|90,000|
|Toyota|Prius G '09|17,700|
