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


# Gran Turismo 7 Shops for 15-June-2025



## Legend shop

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Nissan|Skyline Super Silhouette Group 5 '84|1,150,000|
|Pontiac|GTO 'The Judge' '69|242,000|
|Toyota|2000GT '67|982,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|AMG|300 SEL 6.8 AMG '71|700,000|
|Chevrolet|Corvette (C2) '63|246,000|
|Chevrolet|Corvette Stingray Racer Concept '59|4,000,000|
|Ferrari|F40 '92|3,100,000|
|Ford|Mark IV Race Car '67|6,750,000|
|Jaguar|XJR-9 '88|3,000,000|
|Nissan|R92CP '92|2,000,000|
|Renault|R8 Gordini '66|32,500|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Chevrolet|Corvette Stingray (C3) '69|54,400|
|TVR|Tuscan Speed 6 '00|73,200|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Audi|TT Coupe 3.2 quattro '03|47,400|
|Audi|TTS Coupe '09|55,000|
|BMW|3.0 CSL '73|250,000|
|BMW|M3 '07|72,500|
|Ferrari|308 GTB '75|165,100|
|Ferrari|430 Scuderia '07|358,700|
|Nissan|Fairlady Z 300ZX TT 2seater '89|60,700|
|Peugeot|205 GTI '88|57,400|
|Porsche|911 Carrera RS (964) '92|225,000|
|Renault|Clio V6 24V '00|75,200|
|Toyota|MR2 GT-S '97|51,100|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|MiTo '09|20,600|
|BMW|3.0 CSL '71|137,400|
|BMW|M3 '03|67,800|
|Chevrolet|Corvette Convertible (C3) '69|65,000|
|Chevrolet|Corvette Stingray (C3) '69|71,500|
|Chevrolet|Corvette ZR-1 (C4) '89|105,000|
|Chevrolet|Corvette ZR1 (C6) '09|107,300|
|De Tomaso|Pantera '71|165,000|
|Ferrari|F430 '06|202,200|
|Honda|Integra Type R (DC2) '95|55,600|
|Honda|NSX Type R '02|440,400|
|Nissan|GT-R NISMO (R32) '90|387,200|
|Nissan|SILVIA spec-R Aero (S15) '02|58,200|
|Nissan|Silvia Q's (S13) '88|28,800|
|Suzuki|Cappuccino (EA11R) '91|16,500|
|Toyota|Prius G '09|19,600|
|Volkswagen|Volkswagen 1200 '66|30,400|
