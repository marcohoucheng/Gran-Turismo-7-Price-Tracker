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


# Gran Turismo 7 Shops for 28-May-2025



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|8C 2900B Touring Berlinetta '38|20,000,000|
|Peugeot|205 Turbo 16 Evolution 2 '86|1,000,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Aston Martin|DB3S '53|6,000,000|
|McLaren|McLaren F1 '94|20,000,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Abarth|1500 Biposto Bertone B.A.T 1 '52|1,000,000|
|De Tomaso|Mangusta (Christian Dior)|500,000|
|Ferrari|365 GTB4 '71|610,000|
|Mercedes-Benz|300 SL Coupe '54|1,700,000|
|Mercedes-Benz|CLK-LM '98|8,500,000|
|Nissan|Skyline 2000GT-R (KPGC110) '73|542,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Ferrari|458 Italia '09|252,200|
|Honda|NSX Type R '92|399,200|
|Nissan|R32 GT-R V-spec II '94|171,400|
|Nissan|Skyline GTS-R (R31) '87|171,900|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Abarth|Abarth 500 '09|21,700|
|BMW|M3 '97|84,200|
|Chevrolet|Corvette ZR-1 (C4) '89|88,100|
|Ferrari|Dino 246 GT '71|330,500|
|Ford|Mustang Mach 1 '71|36,200|
|Mazda|RX-7 GT-X (FC) '90|62,900|
|Mitsubishi|GTO Twin Turbo '91|42,300|
|Porsche|911 Carrera RS CS (993) '95|436,200|
|Toyota|Corolla Levin 1600GT APEX (AE86) '83|47,400|
|Toyota|Supra 3.0GT Turbo A '88|116,800|
|Volvo|240 SE Estate '93|48,700|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Audi|R8 4.2 '07|143,500|
|Chevrolet|Corvette Z06 (C5) '01|54,200|
|Chevrolet|Corvette ZR1 (C6) '09|107,700|
|Daihatsu|Copen '02|13,300|
|Dodge|Super Bee '70|67,800|
|Dodge|Viper SRT10 Coupe '06|112,300|
|Fiat|500 1.2 8V Lounge SS '08|13,800|
|Ford|Escort RS Cosworth '92|150,000|
|Ford|Escort RS Cosworth '92|150,000|
|Honda|Civic Type R (EK) '97|51,900|
|Honda|Civic Type R (EK) Touring Car|114,600|
|Lamborghini|Gallardo LP 560-4 '08|249,000|
|Pontiac|Firebird Trans Am '78|87,800|
|Suzuki|Swift Sport '07|12,800|
|Toyota|Sports 800 '65|51,400|
|Volkswagen|Golf I GTI '83|43,700|
