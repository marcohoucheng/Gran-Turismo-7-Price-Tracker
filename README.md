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


# Gran Turismo 7 Shops for 24-March-2025



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Chevrolet|Corvette Stingray Racer Concept '59|4,000,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Ferrari|GTO '84|3,500,000|
|Ford|GT40 Mark I '66|6,700,000|
|Mazda|787B '91|3,300,000|
|Mercedes-Benz|300 SL (W194) '52|20,000,000|
|Mercedes-Benz|Sauber Mercedes C9 '89|3,500,000|
|Nissan|R92CP '92|2,000,000|
|Plymouth|Superbird '70|402,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Autobianchi|A112 Abarth '85|29,700|
|Honda|Civic SiR-II (EG) '93|48,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alpine|A110 '72|133,200|
|BMW|M3 '89|88,300|
|Chevrolet|Corvette Stingray (C3) '69|59,400|
|Nissan|Silvia K's Type S (S14) '94|44,900|
|Subaru|Impreza 22B-STi '98|166,500|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|Giulia Sprint GT Veloce '67|179,700|
|Audi|TTS Coupe '09|55,000|
|BMW|M3 '03|67,100|
|BMW|M3 '07|79,400|
|BMW|M3 Sport Evolution '89|172,000|
|De Tomaso|Pantera '71|163,600|
|Ferrari|308 GTB '75|176,700|
|Ferrari|430 Scuderia '07|363,800|
|Ferrari|F430 '06|208,000|
|Fiat|500 F '68|16,400|
|Honda|Integra Type R (DC2) '95|62,100|
|Honda|NSX Type R '02|435,000|
|MINI|Mini-Cooper 'S' '65|36,200|
|Nissan|GT-R NISMO (R32) '90|392,800|
|Nissan|SILVIA spec-R Aero (S15) '02|59,200|
|Porsche|911 Carrera RS (964) '92|207,000|
|TVR|Tuscan Speed 6 '00|84,600|
|Toyota|MR2 GT-S '97|56,200|
|Toyota|Sprinter Trueno 1600GT APEX (AE86) '83|56,700|
|Volkswagen|Scirocco R '10|38,700|
