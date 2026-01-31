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


# Gran Turismo 7 Shops for 31-January-2026



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Ferrari|F50 '95|4,600,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|155 2.5 V6 TI '93|650,000|
|Dodge|Charger R/T 426 Hemi '68|147,000|
|Ford|Mark IV Race Car '67|6,750,000|
|Mercedes-Benz|300 SL Coupe '54|1,650,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Jaguar|XJ220 '92|559,000|
|Plymouth|XNR Ghia Roadster '60|3,000,000|
|Renault|Espace F1 '95|2,000,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|MiTo '09|22,700|
|BMW|Z8 '01|265,800|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|AMG|SLS AMG '10|320,700|
|Ferrari|Testarossa '91|365,800|
|Ford|Mustang Mach 1 '71|40,800|
|Mitsubishi|Lancer Evolution V GSR '98|64,800|
|Nissan|Silvia K's Aero (S14) '96|58,800|
|Pontiac|Firebird Trans Am '78|110,000|
|Porsche|911 Carrera RS (964) '92|253,000|
|Porsche|911 Turbo (930) '81|223,300|
|Suzuki|Cappuccino (EA11R) '91|16,200|
|Toyota|Sprinter Trueno 1600GT APEX (S.Shigeno Version)|99,500|
|Volkswagen|Volkswagen 1200 '66|31,900|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Abarth|Abarth 595 SS '70|50,200|
|Dodge|Super Bee '70|61,100|
|Ferrari|Dino 246 GT '71|359,300|
|Fiat|500 F '68|17,900|
|Fiat|Panda 30 CL '85|14,000|
|Fiat|Panda 30 CL '85|11,800|
|Honda|Civic SiR-II (EG) '93|58,500|
|Honda|Civic Type R (EK) Touring Car|120,700|
|Maserati|GranTurismo S '08|138,200|
|Mazda|RX-7 GT-X (FC) '90|62,800|
|McLaren|MP4-12C '10|184,200|
|Mitsubishi|GTO Twin Turbo '91|44,800|
|Nissan|Fairlady 240ZG (HS30) '71|98,200|
|Nissan|Silvia K's Dia Selection (S13) '90|56,800|
|Porsche|911 Carrera RS CS (993) '95|441,300|
|TVR|Tuscan Speed 6 '00|95,000|
|Toyota|Supra 3.0GT Turbo A '88|105,400|
