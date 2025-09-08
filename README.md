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


# Gran Turismo 7 Shops for 08-September-2025



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Chevrolet|Corvette Stingray Racer Concept '59|4,000,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Ferrari|250 GTO '62|20,000,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|AMG|300 SEL 6.8 AMG '71|700,000|
|Chevrolet|Corvette (C1) '58|107,000|
|Ferrari|F40 '92|3,100,000|
|Ford|Mark IV Race Car '67|6,750,000|
|Jaguar|XJR-9 '88|3,000,000|
|Nissan|Skyline Hard Top 2000GT-R (KPGC10) '70|194,000|
|Pontiac|GTO 'The Judge' '69|242,000|
|Renault|R8 Gordini '66|32,500|
|Toyota|2000GT '67|982,000|
|Toyota|2000GT '67|982,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|BMW|M3 '89|79,000|
|Mercedes-Benz|SLR McLaren '09|523,400|
|Subaru|Impreza 22B-STi '98|166,900|
|Toyota|Supra RZ '97|220,000|
|Toyota|Supra RZ '97|220,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Citroen|BX 19 TRS '87|23,100|
|De Tomaso|Pantera '71|177,300|
|Dodge|Viper GTS '02|103,600|
|Nissan|Fairlady Z 300ZX TT 2seater '89|58,100|
|Renault|Clio V6 24V '00|81,600|
|Renault|Kangoo 1.4 '01|14,100|
|Renault|R5 Turbo '80|152,900|
|Toyota|Prius G '09|20,700|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|BMW|M3 '03|72,500|
|BMW|M3 '07|80,400|
|Chevrolet|Corvette Stingray (C3) '69|64,100|
|Ferrari|430 Scuderia '07|343,200|
|Ferrari|F430 '06|212,700|
|Ford|Sierra RS 500 Cosworth '87|184,900|
|Honda|Beat '91|17,100|
|Honda|Civic Si Extra (EF) '87|57,200|
|Honda|Integra Type R (DC2) '95|67,200|
|Honda|S800 '66|58,000|
|Honda|S800 '66|42,300|
|Nissan|GT-R NISMO (R32) '90|389,500|
|Nissan|R33 GT-R V-spec '97|154,700|
|Nissan|SILVIA spec-R Aero (S15) '02|59,700|
|Porsche|911 Carrera RS (964) '92|208,600|
|Renault|Avantime 3.0 V6 24V '02|39,000|
|Renault|R4 GTL '85|29,200|
|TVR|Tuscan Speed 6 '00|71,500|
|Toyota|MR2 GT-S '97|50,500|
|Toyota|Supra 3.0GT Turbo A '88|130,000|
|Volkswagen|Sambabus Typ 2 '62|55,300|
