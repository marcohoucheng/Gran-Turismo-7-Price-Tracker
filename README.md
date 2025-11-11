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


# Gran Turismo 7 Shops for 11-November-2025



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|De Tomaso|Mangusta '69|310,000|
|Nissan|Fairlady Z 432 '69|312,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Chaparral|2J '70|2,500,000|
|Chevrolet|Corvette (C2) '63|268,000|
|Ferrari|500 Mondial Pinin Farina Coupe '54|2,000,000|
|Porsche|356 A/1500 GS Carrera '56|618,000|
|Porsche|911 GT1 Strassenversion '97|10,000,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Chevrolet|Chevelle SS 454 Sport Coupé '70|146,000|
|Jaguar|E-type Coupe '61|172,000|
|Porsche|917K '70|20,000,000|
|Toyota|Land Cruiser FJ40V '74|44,100|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|BMW|M3 '97|90,000|
|Fiat|500 F '68|17,900|
|Ford|Escort RS Cosworth '92|150,000|
|Honda|Civic SiR-II (EG) '93|58,500|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Chevrolet|Corvette ZR-1 (C4) '89|84,600|
|Ferrari|Testarossa '91|365,800|
|Ford|Mustang Mach 1 '71|40,800|
|Honda|Civic Type R (EK) Touring Car|120,700|
|McLaren|MP4-12C '10|185,500|
|Peugeot|205 GTI '88|54,100|
|Toyota|Supra 3.0GT Turbo A '88|105,400|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Audi|R8 4.2 '07|136,500|
|BMW|Z8 '01|267,200|
|Chevrolet|Corvette ZR1 (C6) '09|99,200|
|Dodge|Super Bee '70|61,100|
|Dodge|Viper SRT10 Coupe '06|115,300|
|Ferrari|Dino 246 GT '71|359,300|
|Maserati|GranTurismo S '08|138,200|
|Mitsubishi|GTO Twin Turbo '91|44,800|
|Mitsubishi|Lancer Evolution IV GSR '96|46,300|
|Nissan|Fairlady 240ZG (HS30) '71|98,200|
|Nissan|R32 GT-R V-spec II '94|173,400|
|Nissan|Silvia K's Dia Selection (S13) '90|56,800|
|Nissan|Skyline GTS-R (R31) '87|169,000|
|Porsche|911 Carrera RS CS (993) '95|441,300|
|Suzuki|Cappuccino (EA11R) '91|16,200|
|Volkswagen|Volkswagen 1200 '66|31,900|
