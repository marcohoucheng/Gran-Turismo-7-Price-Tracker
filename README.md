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


# Gran Turismo 7 Shops for 12-October-2024



## Legend shop

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Ferrari|F50 '95|4,450,000|
|Porsche|356 A/1500 GS GT Carrera Speedster '56|1,600,000|
|Subaru|Impreza Rally Car '98|650,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|GIULIA TZ2 carrozzata da ZAGATO '65|3,800,000|
|Alpine|A220 Race Car '68|330,000|
|Dodge|Challenger R/T '70|214,000|
|Ferrari|330 P4 '67|20,000,000|
|Jeep|Willys MB '45|30,100|
|NISMO|400R '95|1,800,000|
|Porsche|911 Carrera RS (901) '73|750,000|
|Shelby|G.T.350 '65|469,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|MiTo '09|22,700|
|Toyota|Sprinter Trueno 1600GT APEX (AE86) '83|51,900|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|BMW|M3 '97|83,000|
|Daihatsu|Copen '02|15,700|
|Fiat|500 1.2 8V Lounge SS '08|14,400|
|Ford|Mustang Mach 1 '71|36,100|
|Honda|Integra Type R (DC2) '98|61,200|
|Lamborghini|Gallardo LP 560-4 '08|249,200|
|Lamborghini|Murcielago LP 640 '09|340,400|
|Mitsubishi|GTO Twin Turbo '91|55,000|
|Nissan|Fairlady Z (Z34) '08|33,000|
|Nissan|Silvia Q's (S13) '88|40,000|
|Toyota|Sports 800 '65|47,200|
|Volkswagen|Golf I GTI '83|40,500|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alpine|A110 '72|142,200|
|Chevrolet|Corvette Convertible (C3) '69|53,000|
|Dodge|Super Bee '70|63,200|
|Ferrari|512 BB '76|288,600|
|Ferrari|Dino 246 GT '71|333,900|
|Ferrari|F430 '06|207,400|
|Ford|Ford GT '06|397,100|
|Lancia|Stratos '73|499,300|
|MINI|Mini-Cooper 'S' '65|40,800|
|Mazda|Eunos Roadster (NA) '89|35,000|
|Mazda|RX-7 GT-X (FC) '90|58,900|
|Mitsubishi|Lancer Evolution III GSR '95|100,000|
|Mitsubishi|Lancer Evolution IV GSR '96|55,000|
|Mitsubishi|Lancer Evolution V GSR '98|90,000|
|Mitsubishi|Lancer Evolution VI GSR T.M. SCP '99|200,000|
|Mitsubishi|Lancer Evolution VIII MR GSR '04|65,800|
|Nissan|Fairlady Z Version S (Z33) '07|30,800|
|Nissan|Sileighty '98|89,700|
|Nissan|Silvia K's Type S (S14) '94|51,400|
|Nissan|Skyline GTS-R (R31) '87|179,600|
|Suzuki|Swift Sport '07|11,800|
|Toyota|Supra RZ '97|194,000|
