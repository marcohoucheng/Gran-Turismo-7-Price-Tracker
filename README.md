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


# Gran Turismo 7 Shops for 18-November-2024



## Legend shop

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Ferrari|F50 '95|4,450,000|
|Jaguar|XJ220 '92|615,000|
|Mazda|RX500 '70|600,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|155 2.5 V6 TI '93|800,000|
|Chevrolet|Corvette (C2) '63|239,000|
|Ford|Mark IV Race Car '67|6,750,000|
|Mercedes-Benz|190 E 2.5-16 Evolution II '91|280,000|
|Plymouth|XNR Ghia Roadster '60|1,600,000|
|Porsche|356 A/1500 GS Carrera '56|618,000|
|Porsche|959 '87|1,950,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Renault|R5 Turbo '80|151,900|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Audi|R8 4.2 '07|137,100|
|Chevrolet|Corvette Convertible (C3) '69|53,000|
|Chevrolet|Corvette ZR-1 (C4) '89|90,600|
|Fiat|500 F '68|15,500|
|Lamborghini|Gallardo LP 560-4 '08|249,200|
|MINI|Mini-Cooper 'S' '65|40,800|
|Nissan|R32 GT-R V-spec II '94|178,600|
|Nissan|Skyline GTS-R (R31) '87|179,600|
|Porsche|911 Carrera RS CS (993) '95|438,500|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|Giulia Sprint GT Veloce '67|169,000|
|Alfa Romeo|MiTo '09|22,700|
|BMW|M3 Sport Evolution '89|200,000|
|Dodge|Super Bee '70|63,200|
|Ferrari|512 BB '76|288,600|
|Ferrari|Dino 246 GT '71|333,900|
|Ford|Sierra RS 500 Cosworth '87|200,000|
|Honda|Civic Type R (EK) '98|58,100|
|Honda|NSX Type R '92|402,700|
|Lamborghini|Murcielago LP 640 '09|340,400|
|Lancia|Stratos '73|499,300|
|Mazda|RX-7 GT-X (FC) '90|58,900|
|Mitsubishi|Lancer Evolution III GSR '95|100,000|
|Mitsubishi|Lancer Evolution IV GSR '96|55,000|
|Mitsubishi|Lancer Evolution V GSR '98|90,000|
|Mitsubishi|Lancer Evolution VI GSR T.M. SCP '99|200,000|
|Nissan|Fairlady Z (Z34) '08|33,000|
|Nissan|Sileighty '98|89,700|
|Nissan|Silvia Q's (S13) '88|31,800|
|Porsche|911 GT3 (996) '01|155,600|
|Toyota|Prius G '09|18,500|
